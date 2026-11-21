from ..enums import PandasQueryConditionBinderValues


class PandasQueryCondition:
    def __init__(
        self, column: str, value: any, binder: PandasQueryConditionBinderValues
    ):
        self.column = column
        self.value = value
        self.binder = binder
