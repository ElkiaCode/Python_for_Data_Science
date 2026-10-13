from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """This program loads the image "animal.jpeg",
    prints some information about it and displays it after zooming"""
    try:
        array = ft_load("animal.jpeg")
        if array.size == 0:
            return
        print(array)
        result = array[100:500, 450:850, 0]
        print("New shape after slicing:", result.shape)
        print(result)
        plt.imshow(result, cmap="gray")
        plt.show()
    except (IndexError) as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
