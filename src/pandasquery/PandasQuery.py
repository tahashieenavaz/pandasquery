import pandas
from typing import Optional
from pandasquery.conditions import PandasQueryCondition
from pandasquery.conditions import PandasQueryAndCondition
from pandasquery.conditions import PandasQueryOrCondition
from pandasquery.enums import PandasQueryOperatorsEnum
from pandasquery.exceptions import InvalidOperatorInConditionException
from pandasquery.exceptions import EmptyConditionsException
from .PandasColumn import PandasColumn


class PandasQuery:
    def __init__(
        self,
        adam: any,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
    ):
        self.conditions: list[PandasQueryCondition] = []
        self.conditions.append(
            PandasQueryAndCondition(
                adam=adam,
                operatorOrValue=operatorOrValue,
                valueIfNotProvidedBefore=valueIfNotProvidedBefore,
            )
        )

    def andWhere(
        self,
        adam: str,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
    ):
        if len(self.conditions) == 0:
            raise EmptyConditionsException

        self.conditions.append(
            PandasQueryAndCondition(
                adam=adam,
                operatorOrValue=operatorOrValue,
                valueIfNotProvidedBefore=valueIfNotProvidedBefore,
            )
        )

        return self

    def orWhere(
        self,
        adam: str,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
    ):
        if len(self.conditions) == 0:
            raise EmptyConditionsException

        self.conditions.append(
            PandasQueryOrCondition(
                adam=adam,
                operatorOrValue=operatorOrValue,
                valueIfNotProvidedBefore=valueIfNotProvidedBefore,
            )
        )

        return self

    def apply(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        _mask = pandas.Series(True, index=dataframe.index)
        for condition in self.conditions:
            adam, eve, operator = condition.unpack()

            if operator not in PandasQueryOperatorsEnum:
                raise InvalidOperatorInConditionException(operator)

            if isinstance(eve, PandasColumn):
                eve = dataframe[eve.name]
            elif isinstance(eve, str) and (
                eve.startswith("column:") or eve.startswith("col:")
            ):
                value_column_name = eve.split(":")[-1]
                eve = dataframe[value_column_name]

            if isinstance(adam, PandasColumn):
                adam = dataframe[adam.name]
            elif (
                isinstance(adam, str)
                and not adam.startswith("col:")
                and not adam.startswith("column:")
            ):
                adam = dataframe[adam]
            elif isinstance(adam, str) and (
                adam.startswith("col:") or adam.startswith("column:")
            ):
                adam_column_name = adam.split(":")[-1]
                adam = dataframe[adam_column_name]

            if condition.is_and():
                if operator == PandasQueryOperatorsEnum.EqualTo:
                    _mask &= adam == eve
                elif operator == PandasQueryOperatorsEnum.GreaterThan:
                    _mask &= adam > eve
                elif operator == PandasQueryOperatorsEnum.GreaterThanOrEqualTo:
                    _mask &= adam >= eve
                elif operator == PandasQueryOperatorsEnum.LesserThan:
                    _mask &= adam < eve
                elif operator == PandasQueryOperatorsEnum.LesserThanOrEqualTo:
                    _mask &= adam <= eve
            elif condition.is_or():
                if operator == PandasQueryOperatorsEnum.EqualTo:
                    _mask |= adam == eve
                elif operator == PandasQueryOperatorsEnum.GreaterThan:
                    _mask |= adam > eve
                elif operator == PandasQueryOperatorsEnum.GreaterThanOrEqualTo:
                    _mask |= adam >= eve
                elif operator == PandasQueryOperatorsEnum.LesserThan:
                    _mask |= adam < eve
                elif operator == PandasQueryOperatorsEnum.LesserThanOrEqualTo:
                    _mask |= adam <= eve
            else:
                raise Exception(
                    "Unknown condition type was passed. Condition binder must be in {AND, OR}."
                )
        return dataframe[_mask]
