import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Queue the sentence to be spoken
engine.say(" Welcome")
engine.runAndWait()
# Process the speech request and wait until it's finished
name = input(" enter your name:")
engine.say(name)

engine.runAndWait()
engine.say("enter the full name:")
engine.runAndWait()
paragraph = input("enter the full name:")
engine.say(paragraph)
engine.runAndWait()

engine.say("enter your email:")
engine.runAndWait()
email = input(" enter your email:")
k, d, j = 0, 0, 00
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == "."):
                for i in email:
                    if i == i.isspace():

                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == " _" or i == " ." or i == " @":
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:

                    print("correct mail")
                engine.say("this is  a  correct mail mail")
else:
    engine.say("this is  a incorrerct mail")
engine.runAndWait()
engine.say("enter your country code number :")
engine.runAndWait()
code = input("enter your country c code  :  ")
engine.say("enter your mobile number:")
engine.runAndWait()
number = input(code + " enter your number:")
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)
engine.say(location)
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))
if (code == "+91"):
    engine.say(" you are a  citision of india ")
    engine.runAndWait()


else:
    engine.say(" you are a  not citision of india")
engine.runAndWait()
