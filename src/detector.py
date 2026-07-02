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
def find_contours(edges,img):
    op = img.copy()
    contours, _ = cv2.findContours(
    edges,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
    )
    cv2.drawContours(
    op,
    contours,
    -1,
    (0, 255, 0),
    2
    )
    contours = sorted(
    contours,
    key=cv2.contourArea,
    reverse=True
    )

    return op,contours