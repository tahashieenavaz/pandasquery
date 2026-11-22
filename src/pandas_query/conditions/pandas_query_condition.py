from typing import Optional
from pandas_query.enums import PandasQueryConditionBinderValues


class PandasQueryCondition:
    def __init__(
        self,
        column: str,
        valueOrOperator: any,
        valueIfNotProvidedBefore: any = None,
        *,
        binder: Optional[PandasQueryConditionBinderValues] = None,
    ):
        self.column = column
        self.binder = binder

        if valueIfNotProvidedBefore is not None:
            self.operator = valueOrOperator
            self.value = valueIfNotProvidedBefore
        else:
            self.value = valueOrOperator
            self.operator = "="

    def unpack(self) -> tuple[str, any]:
        return (self.column, self.value)

    def is_and(self):
        return self.binder == PandasQueryConditionBinderValues.AND

    def is_or(self):
        return self.binder == PandasQueryConditionBinderValues.OR
