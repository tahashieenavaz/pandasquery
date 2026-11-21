from .pandas_query_condition import PandasQueryCondition
from pandas_query.enums import PandasQueryConditionBinderValues


class PandasQueryOrCondition(PandasQueryCondition):
    def __init__(self, column: str, value: any):
        super().__init__(
            column=column, value=value, binder=PandasQueryConditionBinderValues.OR
        )
