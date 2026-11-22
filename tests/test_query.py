import pandas
from functools import cache
from pandas_query import Query
import pathlib


@cache
def load_data():
    filename = "titanic.csv"
    file_location = pathlib.Path(__file__).parent / filename
    return pandas.read_csv(file_location)


def test_where_method_works_with_single_equal_condition():
    dataframe = load_data()
    assert len(Query().where("Sex", "male").apply(dataframe)) == 573
    assert len(Query().where("Sex", "female").apply(dataframe)) == 314


def test_where_method_works_with_multiple_equal_condition():
    dataframe = load_data()
    male_survived_query = Query().where("Sex", "male").andWhere("Survived", 1)
    female_survived_query = Query().where("Sex", "female").andWhere("Survived", 1)
    assert len(male_survived_query.apply(dataframe)) == 109
    assert len(female_survived_query.apply(dataframe)) == 233
