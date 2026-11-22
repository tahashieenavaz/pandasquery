import pandas
from pandas_query.conditions import PandasQueryCondition
from pandas_query.conditions import PandasQueryAndCondition
from pandas_query.conditions import PandasQueryOrCondition
from typing import Optional
from pandas_query.enums import PandasQueryConditionBinderValues


class Query:
    def __self__(self):
        self.conditions: list[PandasQueryCondition] = []

    def where(
        self,
        column: str,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
        *,
        binder: Optional[PandasQueryConditionBinderValues] = None,
    ):
        if binder is None and len(self.conditions) != 0:
            raise Exception(
                "Binder can be None only for the first condition. Use orWhere or andWhere instead of where over and over again."
            )

        self.conditions.append(
            PandasQueryCondition(
                column=column,
                operatorOrValue=operatorOrValue,
                valueIfNotProvidedBefore=valueIfNotProvidedBefore,
                binder=None,
            )
        )

    def andWhere(
        self,
        column: str,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
    ):
        if len(self.conditions) == 0:
            raise Exception(
                "Please start the conditions using `where` method and continue using auxiliaries such as `andWhere` and `orWhere`."
            )

        self.conditions.append(
            PandasQueryAndCondition(
                column=column,
                operatorOrValue=operatorOrValue,
                valueIfNotProvidedBefore=valueIfNotProvidedBefore,
            )
        )

    def orWhere(
        self,
        column: str,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
    ):
        if len(self.conditions) == 0:
            raise Exception(
                "Please start the conditions using `where` method and continue using auxiliaries such as `andWhere` and `orWhere`."
            )

        self.conditions.append(
            PandasQueryOrCondition(
                column=column,
                operatorOrValue=operatorOrValue,
                valueIfNotProvidedBefore=valueIfNotProvidedBefore,
            )
        )

    def apply(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
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
        return dataframe[_mask]


if __name__ == "__main__":
    Query().on("name", "Taha Shieenavaz")
