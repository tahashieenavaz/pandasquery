import pandas
import pathlib
from functools import cache as cache_function


@cache_function
def load_titanic():
    filename = "titanic.csv"
    print(pathlib.Path(__file__).parent)
    file_location = pathlib.Path(__file__).parent / "data" / filename
    return pandas.read_csv(file_location)
