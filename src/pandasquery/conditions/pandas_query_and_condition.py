from pandasquery.conditions import PandasQueryCondition
from pandasquery.enums import PandasQueryConditionBinderValues
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
