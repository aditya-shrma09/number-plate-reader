import cv2
import numpy as np
def preposesser(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # bi = cv2.bilateralFilter(gray, 9, 75, 75)
    # equal = cv2.equalizeHist(bi)
    return gray
def detect_edges(equal):
    blur = cv2.GaussianBlur(equal, (5,5), 0)
    edges = cv2.Canny(blur, 100, 200)
    kernel = np.ones((7,7), np.uint8)

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
def find_plate(contours, img):
    op = img.copy()
    height = img.shape[0]
    area = img.shape[0] * img.shape[1]
    

    min = area * 0.01  
    maxx = area * 0.08  
    print(f"min_area={min:.0f}, max_area={maxx:.0f}") 

    candidates = []
    rejected = {"area": 0, "ratio": 0, "position": 0, "zero_h": 0}

    for contour in contours[:20]:
        area = cv2.contourArea(contour)
        if area < min or area > maxx:
            rejected["area"] += 1
            continue

        x, y, w, h = cv2.boundingRect(contour)
        if h == 0:
            rejected["zero_h"] += 1
            continue
        ratio = w / float(h)

        if ratio < 3 or ratio > 5.5:
            rejected["ratio"] += 1
            continue
        # if y < height * 0.5:
        #     rejected["position"] += 1
        #     continue

        candidates.append({"contour": contour, "x": x, "y": y, "w": w, "h": h, "area": area, "ratio": ratio})

    print("rejections:", rejected, "| candidates:", len(candidates))
    if not candidates:
        return op
    for c in candidates:
        print(f"x={c['x']}, y={c['y']}, w={c['w']}, h={c['h']}, ratio={c['ratio']:.2f}, area={c['area']}")

    best = max(candidates, key=lambda c: c["area"])  
    x, y, w, h = best["x"], best["y"], best["w"], best["h"]
    cv2.rectangle(op, (x, y), (x + w, y + h), (0, 255, 0), 3)
    return op