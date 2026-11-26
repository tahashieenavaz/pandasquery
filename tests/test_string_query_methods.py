from pandasquery import PandasQuery
from .loaders import load_titanic


def test_starts_with_string_query():
    dataframe = load_titanic()
    miss_query = PandasQuery("col:Name", "startswith", "Miss.")
    assert len(miss_query.apply(dataframe)) == 182
