from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    res = array.copy()
    res = 255 - res
    plt.imshow(res)
    plt.show()
    return res


def ft_red(array: np.ndarray) -> np.ndarray:
    """Changes the color of the image received in red."""
    res = array.copy()
    res[:, :, 1] *= 0
    res[:, :, 2] *= 0
    plt.imshow(res)
    plt.show()
    return res


def ft_green(array: np.ndarray) -> np.ndarray:
    """Changes the color of the image received in green."""
    res = array.copy()
    res[:, :, 0] -= res[:, :, 0]
    res[:, :, 2] -= res[:, :, 2]
    plt.imshow(res)
    plt.show()
    return res


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Changes the color of the image received in blue."""
    res = array.copy()
    res[:, :, 0] = 0
    res[:, :, 1] = 0
    plt.imshow(res)
    plt.show()
    return res


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Changes the color of the image received in grey."""
    res = array.copy()
    grey = np.sum(res, axis=2) / 3
    res[:, :, 0] = res[:, :, 1] = res[:, :, 2] = grey
    plt.imshow(res)
    plt.show()
    return res


def main():
    """This program loads the image "landscape.jpg",
    and transforms it into different colors"""
    try:
        array = ft_load("landscape.jpg")
        if array.size == 0:
            return
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
    except (IndexError, ValueError) as e:
        print(type(e).__name__ + ":", e)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
