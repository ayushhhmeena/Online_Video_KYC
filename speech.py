import speech_recognition as sr
import re

def extract_info(text):
    name_pattern = r"(?:Name: ([\w\s]+))|(?:Name ([\w\s]+))|(?:my name is ([\w\s]+))"
    dob_pattern = r"(?:Date of Birth is (\d{1,2}) (\w+) (\d{4}))"
    address_pattern = r"(?:Address: ([\w\s\.,]+))|(?:address is ([\w\s\.,]+))"

    name_match = re.search(name_pattern, text, re.IGNORECASE)
    dob_match = re.search(dob_pattern, text, re.IGNORECASE)
    address_match = re.search(address_pattern, text, re.IGNORECASE)

    name = None
    if name_match:
        name = next((group for group in name_match.groups() if group is not None), None)

    dob = None
    if dob_match:
        day, month, year = dob_match.groups()[:3]
        dob = f"{day} {month} {year}"

    address = None
    if address_match:
        address = next((group for group in address_match.groups() if group is not None), None)

    return name.strip() if name else None, dob.strip() if dob else None, address.strip() if address else None

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture microphone input for name
while True:
    with sr.Microphone() as source:
        print("Listening for name...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # Capture the audio
        audio = recognizer.listen(source)
        print("Recognizing name...")
        try:
            # Use Google Web Speech API to recognize audio
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            name, _, _ = extract_info(text)
            if name:
                print("Name recognized:", name)
                break  # Break the loop if name is recognized
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Capture microphone input for Date of Birth
while True:
    with sr.Microphone() as source:
        print("Listening for Date of Birth...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # Capture the audio
        audio = recognizer.listen(source)
        print("Recognizing Date of Birth...")
        try:
            # Use Google Web Speech API to recognize audio
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            _, dob, _ = extract_info(text)
            if dob:
                print("Date of Birth recognized:", dob)
                break  # Break the loop if Date of Birth is recognized
        except sr.UnknownValueError:
            print("Speech Recognition was not Successful please try again.")
        except sr.RequestError as e:
            print("Error In SR; {0}".format(e))

# Capture microphone input for Address
while True:
    with sr.Microphone() as source:
        print("Listening for Address...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # Capture the audio
        audio = recognizer.listen(source)
        print("Recognizing Address...")
        try:
            # Use Google Web Speech API to recognize audio
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            _, _, address = extract_info(text)
            if address:
                print("Address recognized:", address)
                break  # Break the loop if Address is recognized
        except sr.UnknownValueError:
            print("Speech Recognition was not Successful please try again.")
        except sr.RequestError as e:
            print("Error In SR; {0}".format(e))

# Extract information from recognized text
name, dob, address = extract_info(text)

# Display extracted information
print("Name:", name)
print("Date of Birth:", dob)
print("Address:", address)