from enum import Enum


class PandasQueryConditionBinderValues(Enum):
    _or: str = "or"
    _and: str = "and"
