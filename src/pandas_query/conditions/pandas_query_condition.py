from ..enums import PandasQueryConditionBinderValues


class PandasQueryCondition:
    def __init__(
        self, column: str, value: any, binder: PandasQueryConditionBinderValues
    ):
        self.column = column
        self.value = value
        self.binder = binder

    def unpack(self):
        return (self.column, self.value, self.binder)

    def is_and(self):
        return self.binder == PandasQueryConditionBinderValues.AND

    def is_or(self):
        return self.binder == PandasQueryConditionBinderValues.OR
