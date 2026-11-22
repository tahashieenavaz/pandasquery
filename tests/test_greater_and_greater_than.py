from pandas_query import Query
from .loaders import load_titanic


def test_works_with_one_greater_than_condition():
    dataframe = load_titanic()
    under_thirty_query = Query().where("Age", "<=", 10)
    assert len(under_thirty_query.apply(dataframe)) == 71
