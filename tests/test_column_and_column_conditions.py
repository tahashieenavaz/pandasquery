from .loaders import load_titanic
from pandasquery import PandasQuery, PandasColumn


def test_it_can_filter_rows_based_on_only_column_vs_column_conditions():
    dataframe = load_titanic()
    fare_greater_than_age_query = PandasQuery().where(
        PandasColumn("Age"), "<", PandasColumn("Fare")
    )
    age_greater_than_or_equal_to_age_query = PandasQuery().where(
        PandasColumn("Age"), ">=", PandasColumn("Fare")
    )

    assert len(fare_greater_than_age_query.apply(dataframe)) == 276
    assert len(age_greater_than_or_equal_to_age_query.apply(dataframe)) == 611
