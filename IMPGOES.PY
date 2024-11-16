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


def get_valid_input(prompt, validation_func):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print("Invalid input, please try again.")
            engine.say("Invalid input, please try again.")
            engine.runAndWait()


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Greet the user
engine.say("Welcome")
engine.runAndWait()

# Get user's name
name = input("Enter your name: ")
engine.say(name)
engine.runAndWait()

# Get paragraph
engine.say("Enter the paragraph")
engine.runAndWait()
paragraph = input("Enter the paragraph: ")
engine.say(paragraph)
engine.runAndWait()

# Validate email
engine.say("Enter your email")
engine.runAndWait()
email = get_valid_input("Enter your email: ", is_valid_email)
engine.say("This is a correct email")
engine.runAndWait()

# Validate Aadhaar number
engine.say("Enter your Aadhaar number")
engine.runAndWait()
aadhaar = get_valid_input("Enter your Aadhaar number: ", is_valid_aadhaar)
engine.say("This is a correct Aadhaar number")
engine.runAndWait()

# Validate mobile number
engine.say("Enter your country code and mobile number")
engine.runAndWait()
country_code = input("Enter your country code: ")
mobile_number = get_valid_input(country_code + " Enter your mobile number: ",
                                lambda number: is_valid_mobile(number, country_code))

# Combine the country code and number
full_number = country_code + mobile_number
pepnumber = phonenumbers.parse(full_number)

# Get the location and carrier information
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
