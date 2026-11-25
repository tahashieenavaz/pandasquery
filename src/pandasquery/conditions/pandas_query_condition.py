from typing import Optional
from pandasquery.enums import PandasQueryConditionTypeEnum
from pandasquery.enums import PandasQueryOperatorsEnum


class PandasQueryCondition:
    def __init__(
        self,
        adam: str,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
        *,
        binder: Optional[PandasQueryConditionTypeEnum] = None,
    ):
        self.adam = adam
        self.binder = binder

        if valueIfNotProvidedBefore is not None:
            self.eve = valueIfNotProvidedBefore
            self.operator = operatorOrValue
        else:
            self.eve = operatorOrValue
            self.operator = PandasQueryOperatorsEnum.EqualTo

    def unpack(self) -> tuple[str, any]:
        return (self.adam, self.eve, self.operator)

    def is_and(self):
        return self.binder == PandasQueryConditionTypeEnum.AND

    def is_or(self):
        return self.binder == PandasQueryConditionTypeEnum.OR

    def __str__(self):
        return f"PandasQueryCondition({self.adam}, {self.operator}, {self.eve})"

    def __repr__(self):
        return self.__str__()
