import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """This function takes a 2D array, prints its shape and returns a
    truncated version of the array"""
    try:
        assert type(family) is list, "family is not a list"
        assert (type(start) is int
                and type(end) is int), "start and/or end are not an int"
        array = np.array(family)
        assert array.ndim == 2, "this array is not in 2 dimensions"
        print("My shape is :", array.shape)
        tmp = array[start:end]
        print("My new shape is :", tmp.shape)
        result = tmp.tolist()
        return result
    except (AssertionError, ValueError) as e:
        print(type(e).__name__ + ":", e)
        return []


def main():
    """Run the tests given in the subject."""
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
