import cv2
from src.detector import preposesser
from src.detector import detect_edges
from src.detector import find_contours

image = cv2.imread("images\stocksnap-car-2592136_1920.jpg")

processed = preposesser(image)
edges = detect_edges(processed)
c_image,c = find_contours(edges,image)
print(image.shape)
print(len(c))
for i, contour in enumerate(c):
    print(f"Contour {i}")
    print("Area:", cv2.contourArea(contour))
    print("Perimeter:", cv2.arcLength(contour, True))
    print("Number of points:", len(contour))
    print("-" * 30)