from pandas_query.conditions import PandasQueryCondition
from pandas_query.enums import PandasQueryConditionBinderValues
from typing import Optional


class PandasQueryAndCondition(PandasQueryCondition):
    def __init__(
        self,
        column: str,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
    ):
        super().__init__(
            column=column,
            operatorOrValue=operatorOrValue,
            valueIfNotProvidedBefore=valueIfNotProvidedBefore,
            binder=PandasQueryConditionBinderValues.AND,
        )
