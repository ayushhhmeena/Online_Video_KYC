import cv2
import pytesseract

# Path to Tesseract executable (change this according to your Tesseract installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_and_extract_text():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    while True:
        ret, frame = cap.read()

        cv2.imshow('Webcam', frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            text = pytesseract.image_to_string(gray)

            print("Extracted Text:")
            print(text)

            cap.release()
            cv2.destroyAllWindows()
            break
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    print("Press 's' to capture image and extract text, press 'q' to quit")
    capture_and_extract_text()

if __name__ == "__main__":
    main()
