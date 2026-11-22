from typing import Optional
from pandas_query.enums import PandasQueryConditionBinderValues
from pandas_query.enums import PandasQueryOperators


class PandasQueryCondition:
    def __init__(
        self,
        column: str,
        operatorOrValue: any,
        valueIfNotProvidedBefore: Optional[any] = None,
        *,
        binder: Optional[PandasQueryConditionBinderValues] = None,
    ):
        self.column = column
        self.binder = binder

        if valueIfNotProvidedBefore is not None:
            self.value = valueIfNotProvidedBefore
            self.operator = operatorOrValue
        else:
            self.value = operatorOrValue
            self.operator = PandasQueryOperators.EqualTo

    def unpack(self) -> tuple[str, any]:
        return (self.column, self.value, self.operator)

    def is_and(self):
        return self.binder == PandasQueryConditionBinderValues.AND

    def is_or(self):
        return self.binder == PandasQueryConditionBinderValues.OR

    def __str__(self):
        return f"PandasQueryCondition({self.column}, {self.operator}, {self.value})"
