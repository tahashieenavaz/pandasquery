import pandas
from pandas_query.conditions import PandasQueryCondition
from pandas_query.conditions import PandasQueryAndCondition
from pandas_query.conditions import PandasQueryOrCondition
from pandas_query.enums import PandasQueryConditionBinderValues


class Query:
    def __self__(self):
        self.conditions: list[PandasQueryCondition] = []

    def _and(self, column: str, value: any):
        self.conditions.append(PandasQueryAndCondition(column=column, value=value))
        return self

    def _or(self, column: str, value: any):
        self.conditions.append(PandasQueryOrCondition(column=column, value=value))
        return self

    def apply(self, dataframe: pandas.DataFrame):
        _mask = pandas.Series(True, index=dataframe.index)
        for condition in self.conditions:
            column, value = condition.unpack()

            if condition.is_and():
                _mask &= dataframe[column] == value
            elif condition.is_or():
                _mask |= dataframe[column] == value
            else:
                raise Exception(
                    "Unknown condition type was passed. Condition binder must be in {_and, _or}."
                )


if __name__ == "__main__":
    Query().on("name", "Taha Shieenavaz")
