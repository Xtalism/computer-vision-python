import cv2
import numpy as np
from numpy.typing import NDArray


def generate_image(
    size: tuple[int, int], color: tuple[int, int, int]
) -> NDArray[np.uint8]:
    rows: int = size[0]
    cols: int = size[1]
    channels: int = size[2]
    pixels = 255**channels

    img: NDArray[np.uint8] = np.ones(shape=(rows, cols, channels), dtype=np.uint8)
    for i in range(channels):
        img[:, :, i] = color[i]
    print(f"RGB color code: {color}")
    print(f"Size of the generated image is: {img.shape}")
    print(f"Pixels: {pixels}")
    return img


channels = [np.random.randint(low=0, high=255) for _ in range(3)]

img: NDArray[np.uint8] = generate_image(
    size=(300, 300, 3),
    color=(channels),
)
cv2.namedWindow("image", cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
cv2.imshow(winname="image", mat=img)
while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
