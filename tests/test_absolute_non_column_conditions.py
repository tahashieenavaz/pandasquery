from .loaders import load_titanic
from pandasquery import PandasQuery


def test_true_number_and_number():
    dataframe = load_titanic()
    total_length = len(dataframe)
    three_bigger_than_two_query = PandasQuery(3, ">", 2)
    assert len(three_bigger_than_two_query.apply(dataframe)) == total_length


def test_false_number_and_number():
    dataframe = load_titanic()
    three_bigger_than_two_query = PandasQuery(3, "<", 2)
    assert len(three_bigger_than_two_query.apply(dataframe)) == 0
