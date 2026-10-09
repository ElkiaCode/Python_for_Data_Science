import sys


def main():
    """Take a string in argument and encodes it into Morse Code"""
    try:
        NESTED_MORSE = {
                        " ": "/",
                        "A": ".-",
                        "B": "-...",
                        "C": "-.-.",
                        "D": "-..",
                        "E": ".",
                        "F": "..-.",
                        "G": "--.",
                        "H": "....",
                        "I": "..",
                        "J": ".---",
                        "K": "-.-",
                        "L": ".-..",
                        "M": "--",
                        "N": "-.",
                        "O": "---",
                        "P": ".--.",
                        "Q": "--.-",
                        "R": ".-.",
                        "S": "...",
                        "T": "-",
                        "U": "..-",
                        "V": "...-",
                        "W": ".--",
                        "X": "-..-",
                        "Y": "-.--",
                        "Z": "--..",
                        "0": "-----",
                        "1": ".----",
                        "2": "..---",
                        "3": "...--",
                        "4": "....-",
                        "5": ".....",
                        "6": "-....",
                        "7": "--...",
                        "8": "---..",
                        "9": "----."
                    }
        if len(sys.argv) == 2:
            s = sys.argv[1]
        assert len(sys.argv) == 2, "the arguments are bad"
        ustr = s.upper()
        result = ""
        for c in ustr:
            if c in NESTED_MORSE:
                result += NESTED_MORSE[c]
            else:
                raise AssertionError("the arguments are bad")
        result = result.rstrip()
        print(result)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
