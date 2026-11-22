import pandas
from functools import cache
from pandas_query import Query


@cache
def load_data():
    filename = "titanic.csv"
    return pandas.read_csv(filename, index_col=0)


def test_ok():
    dataframe = load_data()
    print(Query().where("sex", "male").apply(dataframe))
