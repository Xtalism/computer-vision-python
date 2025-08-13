import cv2
import numpy as np
from numpy.typing import NDArray

img: NDArray[np.uint8] = (np.ones((500, 500), dtype=np.uint8) * 0).astype(np.uint8)

h, w = img.shape
split_number: int = 4
for i in range(split_number):
    if i % 2 == 0:
        img[:, i * w // split_number : (i + 1) * w // split_number] = 255

cv2.namedWindow("image", cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
cv2.imshow(winname="image", mat=img)
while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
