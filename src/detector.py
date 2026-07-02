import cv2
def preposesser(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bi = cv2.bilateralFilter(gray, 9, 75, 75)
    equal = cv2.equalizeHist(bi)
    return equal
def detect_edges(equal):
    blur = cv2.GaussianBlur(equal, (5,5), 0)
    edges = cv2.Canny(blur, 100, 200)
    return edges