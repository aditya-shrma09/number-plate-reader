import cv2
from src.detector import preposesser
from src.detector import detect_edges
from src.detector import find_contours
from src.detector import find_plate

image = cv2.imread("images\stocksnap-car-2592136_1920.jpg")

processed = preposesser(image)
edges = detect_edges(processed)
c_image,c = find_contours(edges,image)
print(image.shape)
print(len(c))
for i, contour in enumerate(c[:20]):

    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    x, y, w, h = cv2.boundingRect(contour)
    # print(x,y,w,h)
    # print(
    #     f"{i}: area={area:.0f}, "
    #     f"vertices={len(approx)}, "
    #     f"ratio={w/h:.2f}, "
    #     f"y={y}"
    # )
a = find_plate(c,image)

a =cv2.resize(a, (800, 600))
cv2.imshow(" ",a)
cv2.waitKey(0)
cv2.destroyAllWindows()

