import pandas
from functools import cache
from pandas_query import Query
import pathlib


@cache
def load_data():
    filename = "titanic.csv"
    file_location = pathlib.Path(__file__).parent / filename
    return pandas.read_csv(file_location, index_col=0)


def test_ok():
    dataframe = load_data()
    print(Query().where("Sex", "male").apply(dataframe))
