import pandas
import pathlib
from functools import cache as cache_function


@cache_function
def load_titanic():
    filename = "titanic.csv"
    file_location = pathlib.Path(__file__) / "tests" / filename
    return pandas.read_csv(file_location)
