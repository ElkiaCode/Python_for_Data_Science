from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def to_number(value: str | float) -> float:
    """Takes a value with k, M or B and transforms it into float"""
    if isinstance(value, (float, int)):
        return float(value)
    units = {"k": 1000, "M": 1000000, "B": 1000000000}
    last = value[-1]
    if last in units:
        return float(value[:-1]) * units[last]
    return float(value)


def main():
    """Load life expectancy and GDP per capita, then plot
    life expectancy against GDP for each country in 1900."""
    try:
        path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        life = load("life_expectancy_years.csv")
        income = load(path)
        if life is None or income is None:
            return
        a = life[["country", "1900"]]
        b = income[["country", "1900"]]
        merged = pd.merge(a, b, on="country", suffixes=("_life", "_income"))
        tmp = merged.dropna()
        x = tmp["1900_income"].apply(to_number)
        y = tmp["1900_life"]
        plt.scatter(x, y, label="countries")
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.ylabel("Life expectancy")
        plt.legend(loc="lower right")
        plt.show()
    except (ValueError, TypeError, KeyError) as e:
        print(type(e).__name__ + ":", e)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
