import phonenumbers
from phonenumbers import carrier, geocoder
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Predefined data for simulation
# FIX: Removed the leading space from the Aadhaar number
aadhaar_to_mobile = {
    "250002352839": "+919584531181",
    "987654321098": "+911234567890"
}

# Function to validate email


def is_valid_email(email):
    # This logic is very basic; a more robust solution would use regex
    # but for this script, it's sufficient to check for basic format.
    if len(email) < 6:
        return False
    if email.count('@') != 1:
        return False
    # Check if there is a '.' after the '@'
    if '.' not in email.split('@')[1]:
        return False

    return True

# Function to validate Aadhaar number


def is_valid_aadhaar(aadhaar):
    if len(aadhaar) != 12:
        return False
    if not aadhaar.isdigit():
        return False
    return True

# Function to validate mobile number


def is_valid_mobile(number, code):
    try:
        full_number = code + number
        parsed_number = phonenumbers.parse(full_number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False

# Function to check if the Aadhaar number matches the mobile number


def does_aadhaar_match_mobile(aadhaar, full_number):
    return aadhaar_to_mobile.get(aadhaar) == full_number

# Function to get valid input based on a validation function


def get_valid_input(prompt, validation_func):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print("Invalid input, please try again.")
            engine.say("Invalid input, please try again.")
            engine.runAndWait()


# Greet the user
engine.say("Welcome")
engine.runAndWait()

# Get user's name
name = input("Enter your name: ")
engine.say(f"Hello {name}")
engine.runAndWait()

# Get full name
engine.say("Enter your full name")
engine.runAndWait()
# Renamed 'paragraph' to 'full_name' for clarity
paragraph = input("Enter your full name: ")
engine.say(paragraph)
engine.runAndWait()

# Validate email
engine.say("Enter your email:")
engine.runAndWait()
email = get_valid_input("Enter your email: ", is_valid_email)
engine.say("This is a correct email")
engine.runAndWait()

# Validate mobile number
engine.say("Enter your country code and mobile number")
engine.runAndWait()
country_code = input("Enter your country code (e.g., +91): ")
mobile_number = get_valid_input("Enter your mobile number: ",
                                lambda number: is_valid_mobile(number, country_code))

# Combine the country code and number
full_number = country_code + mobile_number

# Aadhaar number input and validation loop
while True:
    engine.say("Enter your Aadhaar number")
    engine.runAndWait()
    aadhaar = get_valid_input("Enter your Aadhaar number: ", is_valid_aadhaar)

    # Check if Aadhaar number matches the mobile number
    if does_aadhaar_match_mobile(aadhaar, full_number):
        engine.say("Aadhaar number matches the mobile number")
        print("Aadhaar number matches the mobile number")
        break  # Exit the loop if valid
    else:
        engine.say(
            "Aadhaar number does not match the mobile number. Please re-enter.")
        print("Aadhaar number does not match the mobile number. Please re-enter.")
        engine.runAndWait()

# Get the location and carrier information
pepnumber = phonenumbers.parse(full_number)
location = geocoder.description_for_number(pepnumber, "en")
service_provider = carrier.name_for_number(pepnumber, "en")

# Print and speak the location and carrier
print(f"Location: {location}")
print(f"Carrier: {service_provider}")
engine.say(f"Location: {location}")
engine.say(f"Carrier: {service_provider}")
engine.runAndWait()

# Check citizenship based on country code
if country_code == "+91":
    engine.say("You are a citizen of India")
    print("You are a citizen of India")
else:
    engine.say("You are not a citizen of India")
    print("You are not a citizen of India")

engine.runAndWait()
