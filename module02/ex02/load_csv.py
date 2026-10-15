import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """This function take path as argument,
    writes th dimensions of the data set and returns it"""
    try:
        assert type(path) is str, "Path is not a string"
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except (AssertionError, OSError, ValueError) as e:
        print(type(e).__name__ + ":", e)
        return None
    except Exception as e:
        print(type(e).__mro__, ":")
        return None
