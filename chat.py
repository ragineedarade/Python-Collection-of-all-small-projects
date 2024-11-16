import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier, geocoder
import pyttsx3


def is_valid_email(email):
    if len(email) < 6:
        return False
    if not email[0].isalpha():
        return False
    if email.count('@') != 1:
        return False
    if not (email[-4] == '.' or email[-3] == '.'):
        return False

    for char in email:
        if char.isspace():
            return False
        if char.isalpha() and char.isupper():
            return False
        if not (char.isalnum() or char in "._@"):
            return False
    return True


def is_valid_aadhaar(aadhaar):
    if len(aadhaar) != 12:
        return False
    if not aadhaar.isdigit():
        return False
    return True


def is_valid_mobile(number, code):
    try:
        full_number = code + number
        parsed_number = phonenumbers.parse(full_number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False


def submit():
    name = name_entry.get()
    paragraph = paragraph_entry.get("1.0", tk.END)
    email = email_entry.get()
    aadhaar = aadhaar_entry.get()
    country_code = country_code_entry.get()
    mobile_number = mobile_number_entry.get()

    engine = pyttsx3.init()

    if not is_valid_email(email):
        messagebox.showerror("Error", "Invalid email. Please try again.")
        engine.say("Invalid email. Please try again.")
        engine.runAndWait()
        return

    if not is_valid_aadhaar(aadhaar):
        messagebox.showerror(
            "Error", "Invalid Aadhaar number. Please try again.")
        engine.say("Invalid Aadhaar number. Please try again.")
        engine.runAndWait()
        return

    if not is_valid_mobile(mobile_number, country_code):
        messagebox.showerror(
            "Error", "Invalid mobile number. Please try again.")
        engine.say("Invalid mobile number. Please try again.")
        engine.runAndWait()
        return

    # Combine the country code and number
    full_number = country_code + mobile_number
    pepnumber = phonenumbers.parse(full_number)

    # Get the location and carrier information
    location = geocoder.description_for_number(pepnumber, "en")
    service_provider = carrier.name_for_number(pepnumber, "en")

    messagebox.showinfo(
        "Information", f"Location: {location}\nCarrier: {service_provider}")
    engine.say(f"Location: {location}, Carrier: {service_provider}")
    engine.runAndWait()

    if country_code == "+91":
        messagebox.showinfo("Status", "You are a citizen of India")
        engine.say("You are a citizen of India")
    else:
        messagebox.showinfo("Status", "You are not a citizen of India")
        engine.say("You are not a citizen of India")
    engine.runAndWait()


# Create the main window
root = tk.Tk()
root.title("Citizen Verification")

# Create and place labels and entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, sticky=tk.W)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Paragraph:").grid(row=1, column=0, sticky=tk.W)
paragraph_entry = tk.Text(root, height=5, width=30)
paragraph_entry.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Aadhaar Number:").grid(row=3, column=0, sticky=tk.W)
aadhaar_entry = tk.Entry(root)
aadhaar_entry.grid(row=3, column=1)

tk.Label(root, text="Country Code:").grid(row=4, column=0, sticky=tk.W)
country_code_entry = tk.Entry(root)
country_code_entry.grid(row=4, column=1)

tk.Label(root, text="Mobile Number:").grid(row=5, column=0, sticky=tk.W)
mobile_number_entry = tk.Entry(root)
mobile_number_entry.grid(row=5, column=1)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=6, column=0, columnspan=2)

# Run the application
root.mainloop()
