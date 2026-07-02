import cv2
from src.detector import preposesser
from src.detector import detect_edges
from src.detector import find_contours

image = cv2.imread("images\stocksnap-car-2592136_1920.jpg")

processed = preposesser(image)
edges = detect_edges(processed)

print(image.shape)

display = cv2.resize(image, (800, 600))
processed_display = cv2.resize(edges, (800, 600))

cv2.imshow("Original", display)
cv2.imshow("Processed", processed_display)

cv2.waitKey(0)
cv2.destroyAllWindows()