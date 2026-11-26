from pandasquery import PandasQuery
from .loaders import load_titanic


def test_starts_with_string_query():
    dataframe = load_titanic()
    miss_query = PandasQuery("col:Name", "startswith", "Miss.")
    miss_query_symbol = PandasQuery("col:Name", "^", "Miss.")
    assert len(miss_query.apply(dataframe)) == 182
    assert len(miss_query_symbol.apply(dataframe)) == 182
