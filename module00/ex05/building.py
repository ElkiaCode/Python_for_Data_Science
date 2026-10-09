import sys


def main():
    """return the sums of its upper-case characters, lower-case
characters, punctuation characters, digits, and spaces."""
    try:
        if len(sys.argv) == 1:
            print("What is the text to count?")
            s = sys.stdin.readline()
        elif len(sys.argv) == 2:
            s = sys.argv[1]
        assert len(sys.argv) <= 2, "too many arguments"
        space = 0
        digit = 0
        upper = 0
        lower = 0
        punctuation = 0
        for c in s:
            if c.isspace():
                space += 1
            elif c.isdigit():
                digit += 1
            elif c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
            else:
                punctuation += 1
        print("The text contains " + str(len(s)) + " characters:")
        print(str(upper) + " upper letters")
        print(str(lower) + " lower letters")
        print(str(punctuation) + " punctuation marks")
        print(str(space) + " spaces")
        print(str(digit) + " digits")
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
