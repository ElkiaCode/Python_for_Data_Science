import sys


def main():
    try:
        if len(sys.argv) == 1:
            return
        assert len(sys.argv) == 2, "more than one argument is provided"
        try:
            n = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
