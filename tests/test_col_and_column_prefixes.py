from .loaders import load_titanic
from pandasquery import PandasQuery


def test_it_can_filter_rows_based_on_only_column_vs_column_conditions_with_string_prefixes():
    dataframe = load_titanic()
    fare_greater_than_age_query = PandasQuery("column:Age", "<", "column:Fare")
    age_greater_than_or_equal_to_age_query = PandasQuery("col:Age", ">=", "col:Fare")

    assert len(fare_greater_than_age_query.apply(dataframe)) == 276
    assert len(age_greater_than_or_equal_to_age_query.apply(dataframe)) == 611
