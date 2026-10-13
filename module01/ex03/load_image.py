import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """This function loads an image, prints its pixels content
    in RGB format."""
    try:
        assert type(path) is str, "path is not a string"
        img = Image.open(path)
        new_img = img.convert("RGB")
        result = np.array(new_img)
        print("The shape of image is:", result.shape)
        return result
    except (AssertionError, OSError) as e:
        print(type(e).__name__ + ":", e)
        return np.array([])
