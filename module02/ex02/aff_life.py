from load_csv import load
import matplotlib.pyplot as plt


def to_number(value: str) -> float:
    """Take a value with k, M or B and transforms it into float"""
    units = {"k": 1000, "M": 1000000, "B": 1000000000}
    last = value[-1]
    if last in units:
        return float(value[:-1]) * units[last]
    return float(value)


def main():
    """This program loads a .csv and displays the France information
    and compares it with Belgium"""
    try:
        df = load("population_total.csv")
        if df is None:
            return
        fr = df[df["country"] == "France"]
        bel = df[df["country"] == "Belgium"]
        serie_fr = fr.iloc[0, 1:]
        serie_bel = bel.iloc[0, 1:]
        cut_fr = serie_fr.loc["1800":"2050"]
        cut_bel = serie_bel.loc["1800":"2050"]
        x_fr = cut_fr.index.astype(int)
        x_bel = cut_bel.index.astype(int)
        y_fr = cut_fr.apply(to_number)
        y_bel = cut_bel.apply(to_number)
        plt.plot(x_fr, y_fr, label="France")
        plt.plot(x_bel, y_bel, label="Belgium")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc="lower right")
        plt.show()
    except (IndexError, ValueError, TypeError) as e:
        print(type(e).__name__ + ":", e)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
