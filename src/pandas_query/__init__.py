from pandas_query.conditions import PandasQueryCondition
from pandas_query.conditions import PandasQueryAndCondition
from pandas_query.conditions import PandasQueryOrCondition


class Query:
    def __self__(self):
        self.conditions: list[PandasQueryCondition] = []

    def _and(self, column: str, value: any):
        self.conditions.append(PandasQueryAndCondition(column=column, value=value))
        return self

    def _or(self, column: str, value: any):
        Query.conditions.append(PandasQueryOrCondition(column=column, value=value))
        return self


if __name__ == "__main__":
    Query.on("name", "Taha Shieenavaz")
