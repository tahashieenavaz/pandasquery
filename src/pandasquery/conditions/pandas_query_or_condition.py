from typing import Optional
from pandasquery.enums import PandasQueryConditionTypeEnum
from .pandas_query_condition import PandasQueryCondition


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
            binder=PandasQueryConditionTypeEnum.OR,
        )
