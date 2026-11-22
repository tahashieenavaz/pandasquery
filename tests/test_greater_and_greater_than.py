from pandasquery import Query
from .loaders import load_titanic


def test_greater_than_conditions_work_with_single_condition():
    dataframe = load_titanic()
    above_thirty_query = Query().where("Age", ">", 30)
    thirty_and_above_thirty_query = Query().where("Age", ">=", 30)
    assert len(above_thirty_query.apply(dataframe)) == 362
    assert len(thirty_and_above_thirty_query.apply(dataframe)) == 395


def test_greater_than_conditions_work_with_multiple_condition():
    dataframe = load_titanic()
    above_thirty_females_query = Query().where("Age", ">", 30).andWhere("Sex", "female")
    thirty_and_above_thirty_males_query = (
        Query().where("Age", ">=", 30).andWhere("Sex", "male")
    )
    assert len(above_thirty_females_query.apply(dataframe)) == 122
    assert len(thirty_and_above_thirty_males_query.apply(dataframe)) == 262
