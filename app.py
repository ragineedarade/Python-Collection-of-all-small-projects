from flask import Flask, request, render_template, jsonify
import phonenumbers
from phonenumbers import carrier, geocoder

app = Flask(__name__)


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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    email = data['email']
    aadhaar = data['aadhaar']
    country_code = data['country_code']
    mobile_number = data['mobile_number']

    if not is_valid_email(email):
        return jsonify({'status': 'error', 'message': 'Invalid email'})

    if not is_valid_aadhaar(aadhaar):
        return jsonify({'status': 'error', 'message': 'Invalid Aadhaar number'})

    if not is_valid_mobile(mobile_number, country_code):
        return jsonify({'status': 'error', 'message': 'Invalid mobile number'})

    # Combine the country code and number
    full_number = country_code + mobile_number
    pepnumber = phonenumbers.parse(full_number)

    # Get the location and carrier information
    location = geocoder.description_for_number(pepnumber, "en")
    service_provider = carrier.name_for_number(pepnumber, "en")

    if country_code == "+91":
        citizenship = "You are a citizen of India"
    else:
        citizenship = "You are not a citizen of India"

    return jsonify({
        'status': 'success',
        'location': location,
        'service_provider': service_provider,
        'citizenship': citizenship
    })


if __name__ == '__main__':
    app.run(debug=True)
