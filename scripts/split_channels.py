import cv2
import numpy as np
from numpy.typing import NDArray


def split_channels(
    path,
) -> NDArray[np.uint8]:
    img = cv2.imread(path)
    channels = tuple(img[:, :, i] for i in range(img.shape[2]))
    return channels


if __name__ == "__main__":
    channels = split_channels("pictures/kanye.jpg")

    cv2.imshow(winname="original", mat=cv2.imread("pictures/kanye.jpg"))

    for i in range(3):
        cv2.namedWindow(f"image{i}", cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
        cv2.imshow(winname=f"image{i}", mat=channels[i])

    while True:
        if cv2.waitKey(0) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()
