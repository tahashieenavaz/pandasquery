from enum import Enum


class PandasQueryConditionBinderValues(Enum):
    OR: str = "or"
    AND: str = "and"
