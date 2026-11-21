from pandas_query.conditions import PandasQueryCondition
from pandas_query.enums import PandasQueryConditionBinderValues


class PandasQueryAndCondition(PandasQueryCondition):
    def __init__(self, column: str, value: any):
        super().__init__(
            column=column, value=value, binder=PandasQueryConditionBinderValues.AND
        )
