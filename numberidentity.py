from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers
number = " 7898083704"
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))
