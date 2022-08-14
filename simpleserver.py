from asyncio.windows_events import NULL
from flask import Flask
from PIL import Image
import pytesseract
import numpy as np
import cv2
import werkzeug

app = Flask(__name__)

@app.route('/')
def index():
    filename = 'image1.png'
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = cv2.imread("image1.png")
    if img is None:
        return "null"
    img = cv2.resize(img, (400, 450))
    #cv2.imshow("Image", img)
    text = pytesseract.image_to_string(img)
    # print(text)
    return text

def post(self):
    # read like a stream
    data = request.files['file']
    img = Image.open(request.files['file'])
    img = np.array(img)
    # convert numpy array to image
    cv2.imwrite("saved_file.jpg", img)

if __name__ == '__main__':
    app.run(debug=True)



