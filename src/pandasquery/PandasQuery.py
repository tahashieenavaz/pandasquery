import pandas
from typing import Optional
from pandasquery.conditions import PandasQueryCondition
from pandasquery.conditions import PandasQueryAndCondition
from pandasquery.conditions import PandasQueryOrCondition
from pandasquery.enums import PandasQueryConditionTypeEnum
from pandasquery.enums import PandasQueryOperatorsEnum
from pandasquery.exceptions import InvalidOperatorInConditionException
from pandasquery.exceptions import EmptyConditionsException
from .PandasColumn import PandasColumn


class PandasQuery:
    def __init__(
        self,
        column: str | PandasColumn,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
    ):

        self.conditions: list[PandasQueryCondition] = []
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
            raise EmptyConditionsException

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
            raise EmptyConditionsException

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
                raise InvalidOperatorInConditionException(operator)

            if isinstance(value, PandasColumn):
                value = dataframe[value.name]
            elif isinstance(value, str) and (
                value.startswith("column:") or value.startswith("col:")
            ):
                value_column_name = value.split(":")[-1]
                value = dataframe[value_column_name]

            if isinstance(column, PandasColumn):
                column = dataframe[column.name]
            elif (
                isinstance(column, str)
                and not column.startswith("col:")
                and not column.startswith("column:")
            ):
                column = dataframe[column]
            elif isinstance(column, str) and (
                column.startswith("col:") or column.startswith("column:")
            ):
                column_column_name = column.split(":")[-1]
                column = dataframe[column_column_name]

            if condition.is_and():
                if operator == PandasQueryOperatorsEnum.EqualTo:
                    _mask &= column == value
                elif operator == PandasQueryOperatorsEnum.GreaterThan:
                    _mask &= column > value
                elif operator == PandasQueryOperatorsEnum.GreaterThanOrEqualTo:
                    _mask &= column >= value
                elif operator == PandasQueryOperatorsEnum.LesserThan:
                    _mask &= column < value
                elif operator == PandasQueryOperatorsEnum.LesserThanOrEqualTo:
                    _mask &= column <= value
            elif condition.is_or():
                if operator == PandasQueryOperatorsEnum.EqualTo:
                    _mask |= column == value
                elif operator == PandasQueryOperatorsEnum.GreaterThan:
                    _mask |= column > value
                elif operator == PandasQueryOperatorsEnum.GreaterThanOrEqualTo:
                    _mask |= column >= value
                elif operator == PandasQueryOperatorsEnum.LesserThan:
                    _mask |= column < value
                elif operator == PandasQueryOperatorsEnum.LesserThanOrEqualTo:
                    _mask |= column <= value
            else:
                raise Exception(
                    "Unknown condition type was passed. Condition binder must be in {AND, OR}."
                )
        return dataframe[_mask]
