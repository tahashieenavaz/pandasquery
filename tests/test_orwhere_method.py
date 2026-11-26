from pandasquery import PandasQuery
from .loaders import load_titanic


def test_orwhere_query():
    dataframe = load_titanic()
    miss_or_graham_query = PandasQuery("col:Name", "^", "Miss.").orWhere(
        "col:Name", "endswith", "Graham"
    )
    miss_query = PandasQuery("col:Name", "startswith", "Miss.")
    graham_query = PandasQuery("col:Name", "endswith", "Graham")
    miss_graham_query = PandasQuery("col:Name", "startswith", "Miss.").andWhere(
        "col:Name", "endswith", "Graham"
    )
    miss_length = len(miss_query.apply(dataframe))
    graham_length = len(graham_query.apply(dataframe))
    miss_graham_length = len(miss_graham_query.apply(dataframe))
    assert (
        len(miss_or_graham_query.apply(dataframe))
        == miss_length + graham_length - miss_graham_length
    )
