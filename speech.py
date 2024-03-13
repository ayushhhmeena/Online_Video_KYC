import speech_recognition as sr
import re

def extract_info(text):
    name_pattern = r"(?:Name: ([\w\s]+))|(?:Name ([\w\s]+))|(?:my name is ([\w\s]+))"
    dob_pattern = r"DOB: (\d{2}/\d{2}/\d{4})"
    address_pattern = r"Address: ([\w\s\.,]+)"
    name_match = re.search(name_pattern, text, re.IGNORECASE)
    dob_match = re.search(dob_pattern, text)
    address_match = re.search(address_pattern, text)
    name = None
    if name_match:
        name = next(group for group in name_match.groups() if group is not None)
    dob = dob_match.group(1) if dob_match else None
    address = address_match.group(1) if address_match else None
    return name, dob, address

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture microphone input
while True:
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # Capture the audio
        audio = recognizer.listen(source)
        print("Recognizing...")
        try:
            # Use Google Web Speech API to recognize audio
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            break  # Break the loop if recognition is successful
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Extract information from recognized text
name, dob, address = extract_info(text)

# Display extracted information
print("Name:", name)
print("DOB:", dob)
print("Address:", address)
