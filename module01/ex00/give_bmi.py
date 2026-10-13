def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Take two lists (height and weight) and return the list of BMI."""
    try:
        assert isinstance(height, list), "height must be a list"
        assert isinstance(weight, list), "weight must be a list"
        assert len(height) == len(weight), "the lists must have the same size"
        for h, w in zip(height, weight):
            if type(h) not in (int, float) or type(w) not in (int, float):
                raise AssertionError("values must be int or float")
        assert all(x > 0 for x in height), "height values must be positive"
        assert all(x > 0 for x in weight), "weight values must be positive"
        bmi = [w / h ** 2 for w, h in zip(weight, height)]
        return bmi
    except AssertionError as e:
        print("AssertionError:", e)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """For each BMI, the function returns True
    if it is above the limit, and False otherwise"""
    try:
        assert isinstance(bmi, list), "bmi must be a list"
        for v in bmi:
            if type(v) not in (int, float):
                raise AssertionError("argument is not an int or float")
        assert all(x > 0 for x in bmi), "not a positive int or float"
        assert type(limit) is int, "limit is not an int"
        assert limit >= 0, "limit much be a positive int or 0"
        res = [x > limit for x in bmi]
        return res
    except AssertionError as e:
        print("AssertionError:", e)
        return []


def main():
    """Run the test given in the subject."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
