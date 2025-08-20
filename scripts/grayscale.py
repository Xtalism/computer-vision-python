import cv2
import numpy as np
from numpy.typing import NDArray


def grayscale(path) -> NDArray[np.uint8]:
    img = cv2.imread(path)
    gray: NDArray[np.uint8] = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


if __name__ == "__main__":
    gray = grayscale("pictures/kanye.jpg")

    cv2.namedWindow("image", cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
    cv2.imshow(winname="image", mat=gray)

    while True:
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()
