from pandasquery import Query
from .loaders import load_titanic


def test_where_method_works_with_single_equal_condition():
    dataframe = load_titanic()
    assert len(Query().where("Sex", "male").apply(dataframe)) == 573
    assert len(Query().where("Sex", "female").apply(dataframe)) == 314


def test_where_method_works_with_multiple_equal_condition():
    dataframe = load_titanic()
    male_survived_query = Query().where("Sex", "male").andWhere("Survived", 1)
    female_survived_query = Query().where("Sex", "female").andWhere("Survived", 1)
    assert len(male_survived_query.apply(dataframe)) == 109
    assert len(female_survived_query.apply(dataframe)) == 233
