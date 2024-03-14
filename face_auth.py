import cv2
import face_recognition
import sys
def take_picture():
    print("Scanning Face...")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('Picture.jpg', frame)
    cv2.destroyAllWindows()
    cap.release()
    print("Face scan complete.")

def analyze_user():
    print("Analyzing Face...")
    # Picture of Me as a baseline comparison
    baseimg = face_recognition.load_image_file("D:\Code\KYC\10004.jpeg")
    baseimg = cv2.cvtColor(baseimg, cv2.COLOR_BGR2RGB)

    myface = face_recognition.face_locations(baseimg)[0]
    encodemyface = face_recognition.face_encodings(baseimg)[0]
    cv2.rectangle(baseimg, (myface[3], myface[0]), (myface[1], myface[2]), (255, 0, 255), 2)

    # Sample image of face picture
    sampleimg = face_recognition.load_image_file("Picture.jpg")
    sampleimg = cv2.cvtColor(sampleimg, cv2.COLOR_BGR2RGB)
    samplefacetest = face_recognition.face_locations(sampleimg)[0]
    try:
        encodesamplefacetest = face_recognition.face_encodings(sampleimg)[0]
    except IndexError as e:
        print("Index Error. Authentication Failed.")
        sys.exit()

    result = face_recognition.compare_faces([encodemyface], encodesamplefacetest)
    resultstring = str(result)

    if resultstring == "[True]":
        print("User Authenticated. Welcome back sir!")
    else:
        print("Authentication Failed. Good bye!")

take_picture()
analyze_user()
