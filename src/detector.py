import cv2
import numpy as np
def preposesser(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bi = cv2.bilateralFilter(gray, 9, 75, 75)
    equal = cv2.equalizeHist(bi)
    return equal
def detect_edges(equal):
    blur = cv2.GaussianBlur(equal, (5,5), 0)
    edges = cv2.Canny(blur, 100, 200)
    kernel = np.ones((5, 5), np.uint8)

    closed = cv2.morphologyEx(
        edges,
        cv2.MORPH_CLOSE,
        kernel)
    return closed
def find_contours(closed,img):
    op = img.copy()
    contours, _ = cv2.findContours(
    closed,
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
def find_plate(contours,img):
    op = img.copy()
    for contour in contours[:20]:
        perimeter = cv2.arcLength(contour, True)

        approx = cv2.approxPolyDP(
            contour,
            0.02 * perimeter,
            True)
        if len(approx) == 4:
            return cv2.drawContours(op, [approx], -1, (0, 255, 0), 3)
       