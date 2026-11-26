from pandasquery import PandasQuery
from .loaders import load_titanic


def test_startswith_string_query():
    dataframe = load_titanic()
    miss_query = PandasQuery("col:Name", "startswith", "Miss.")
    miss_query_symbol = PandasQuery("col:Name", "^", "Miss.")
    assert len(miss_query.apply(dataframe)) == 182
    assert len(miss_query_symbol.apply(dataframe)) == 182


def test_endswith_string_query():
    dataframe = load_titanic()
    miss_query = PandasQuery("col:Name", "endswith", "Graham")
    miss_query_symbol = PandasQuery("col:Name", "$", "Graham")
    assert len(miss_query.apply(dataframe)) == 3
    assert len(miss_query_symbol.apply(dataframe)) == 3
