from pandas_query import Query
from .loaders import load_titanic


def test_works_with_one_greater_than_condition():
    dataframe = load_titanic()
    above_thirty_query = Query().where("Age", ">", 30)
    thirty_and_above_thirty_query = Query().where("Age", ">=", 30)
    assert len(above_thirty_query.apply(dataframe)) == 362
    assert len(thirty_and_above_thirty_query.apply(dataframe)) == 395
