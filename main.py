from PIL import Image
import pytesseract
import cv2
import numpy as np

# Load the image using OpenCV
image_path = 'test1.png'
image = cv2.imread(image_path)

# Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# (Optional) Apply thresholding to binarize the image
# _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Convert the image to PIL format (pytesseract requires PIL format)
# pil_image = Image.fromarray(thresh)

# Extract text using pytesseract
text = pytesseract.image_to_string(image)

print("Extracted Text:\n", text)

