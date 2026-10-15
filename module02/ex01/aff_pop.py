from load_csv import load
import matplotlib.pyplot as plt


def main():
    """This program loads a .csv and displays the France information"""
    try:
        df = load("life_expectancy_years.csv")
        if df is None:
            return
        fr = df[df["country"] == "France"]
        serie = fr.iloc[0, 1:]
        x = serie.index.astype(int)
        y = serie.values.astype(float)
        plt.plot(x, y)
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except IndexError as e:
        print(type(e).__name__ + ":", e)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
