import sys


def main():
    """this function output a list
    of words from S that have a length greater than N"""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        try:
            n = int(sys.argv[2])
            s = sys.argv[1]
        except ValueError:
            raise AssertionError("the arguments are bad")
        words = s.split()
        m = [m for m in words if (lambda w: len(w) > n)(m)]
        print(m)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
