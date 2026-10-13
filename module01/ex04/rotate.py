from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_transpose(array: np.ndarray) -> np.ndarray:
    """Transpose a 2D array by hand: rows become columns.
    Return a new array of shape (x, y) from an array of shape (y, x)."""
    y_old, x_old = array.shape
    res = np.zeros((x_old, y_old), dtype=array.dtype)
    for i in range(x_old):
        for j in range(y_old):
            res[i][j] = array[j][i]
    return res


def main():
    """This program loads the image "animal.jpeg",
    prints some information about it and displays it after transposing it"""
    try:
        array = ft_load("animal.jpeg")
        if array.size == 0:
            return
        tmp = array[100:500, 450:850, 0]
        print("The shape of image is:", tmp.shape)
        print(tmp)
        result = ft_transpose(tmp)
        print("New shape after Transpose:", result.shape)
        print(result)
        plt.imshow(result, cmap="gray")
        plt.show()
    except (IndexError, ValueError) as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
