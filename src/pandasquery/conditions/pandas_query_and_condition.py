from typing import Optional
from pandasquery.conditions import PandasQueryCondition
from pandasquery.enums import PandasQueryConditionTypeEnum


class PandasQueryAndCondition(PandasQueryCondition):
    def __init__(
        self,
        adam: any,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
    ):
        super().__init__(
            column=adam,
            operatorOrValue=operatorOrValue,
            valueIfNotProvidedBefore=valueIfNotProvidedBefore,
            binder=PandasQueryConditionTypeEnum.AND,
        )
