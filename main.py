import cv2

from src.detector import (
    preposesser,
    detect_edges,
    find_contours,
    find_plate
)

from src.ocr import read_plate

image = cv2.imread("images/stocksnap-car-2592136_1920.jpg")

processed = preposesser(image)
edges = detect_edges(processed)

_, contours = find_contours(edges, image)

plate = find_plate(contours, image)
cv2.imshow("Plate", plate)


cv2.waitKey(0)
cv2.destroyAllWindows()

if plate is not None:
    text = read_plate(plate)
    print("Detected Plate:", text)
else:
    print("No plate detected.")