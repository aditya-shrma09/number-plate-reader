import cv2
def preposesser(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bi = cv2.bilateralFilter(gray, 9, 75, 75)
    equal = cv2.equalizeHist(bi)
    return equal