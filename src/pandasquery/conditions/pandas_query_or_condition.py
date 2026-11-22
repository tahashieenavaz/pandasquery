from .pandas_query_condition import PandasQueryCondition
from pandasquery.enums import PandasQueryConditionBinderValues
from typing import Optional


class PandasQueryOrCondition(PandasQueryCondition):
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
            binder=PandasQueryConditionBinderValues.OR,
        )
