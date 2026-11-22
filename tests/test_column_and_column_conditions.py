from .loaders import load_titanic
from pandasquery import PandasQuery, PandasColumn


def test_it_can_filter_rows_based_on_only_column_vs_column_conditions():
    dataframe = load_titanic()

    print(
        PandasQuery()
        .where(PandasColumn("Age"), ">=", PandasColumn("Fare"))
        .apply(dataframe)
    )
