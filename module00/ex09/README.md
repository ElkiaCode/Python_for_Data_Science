# ft_package

A small Python package that counts how many times a value appears in a list.
Created as the last exercise of the *Piscine Python for Data Science* (module 00), 42 Nice.

## Installation

From the `ex09/` directory, build the package:

```bash
pip install build
python3 -m build
```

Then install it with one of these two commands:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Check the installation:

```bash
pip list | grep ft_package
pip show -v ft_package
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```

## API

`count_in_list(lst, value)`

- `lst`: the list to search in.
- `value`: the value to count.
- Returns the number of items in `lst` equal to `value`, as an `int`.

## Requirements

- Python 3.10 or higher.

## License

Distributed under the MIT license. See the `LICENSE` file.

## Author

Clement Parodi, 42 Nice.