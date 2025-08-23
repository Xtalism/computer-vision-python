import cv2
import numpy as np
from numpy.typing import NDArray

if __name__ == "__main__":
    img = cv2.imread("pictures/kanye.jpg")
    gray: NDArray[np.uint8] = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow("image", cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
    cv2.imshow(winname="image", mat=gray)

    while True:
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()
