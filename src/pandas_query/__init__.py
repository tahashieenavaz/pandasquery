import pandas
from pandas_query.conditions import PandasQueryCondition
from pandas_query.conditions import PandasQueryAndCondition
from pandas_query.conditions import PandasQueryOrCondition
from typing import Optional
from pandas_query.enums import PandasQueryConditionBinderValues
from pandas_query.enums import PandasQueryOperatorsEnum


class Query:
    def __init__(self):
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
            PandasQueryAndCondition(
                column=column,
                operatorOrValue=operatorOrValue,
                valueIfNotProvidedBefore=valueIfNotProvidedBefore,
            )
        )

        return self

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

        return self

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

        return self

    def apply(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        _mask = pandas.Series(True, index=dataframe.index)
        for condition in self.conditions:
            column, value, operator = condition.unpack()

            if operator not in PandasQueryOperatorsEnum:
                raise Exception(f"Invalid operator found in conditions. {operator}")

            if condition.is_and():
                if operator == PandasQueryOperatorsEnum.EqualTo:
                    _mask &= dataframe[column] == value
                elif operator == PandasQueryOperatorsEnum.GreaterThan:
                    _mask &= dataframe[column] > value
                elif operator == PandasQueryOperatorsEnum.GreaterThanOrEqualTo:
                    _mask &= dataframe[column] >= value
                elif operator == PandasQueryOperatorsEnum.LesserThan:
                    _mask &= dataframe[column] < value
                elif operator == PandasQueryOperatorsEnum.LesserThanOrEqualTo:
                    _mask &= dataframe[column] <= value
            elif condition.is_or():
                if operator == PandasQueryOperatorsEnum.EqualTo:
                    _mask |= dataframe[column] == value
                elif operator == PandasQueryOperatorsEnum.GreaterThan:
                    _mask |= dataframe[column] > value
                elif operator == PandasQueryOperatorsEnum.GreaterThanOrEqualTo:
                    _mask |= dataframe[column] >= value
                elif operator == PandasQueryOperatorsEnum.LesserThan:
                    _mask |= dataframe[column] < value
                elif operator == PandasQueryOperatorsEnum.LesserThanOrEqualTo:
                    _mask |= dataframe[column] <= value
            else:
                raise Exception(
                    "Unknown condition type was passed. Condition binder must be in {AND, OR}."
                )
        return dataframe[_mask]


if __name__ == "__main__":
    Query().on("name", "Taha Shieenavaz")
