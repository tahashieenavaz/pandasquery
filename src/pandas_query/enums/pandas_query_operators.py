from enum import Enum


class PandasQueryOperators(Enum):
    GreaterThan = ">"
    LesserThan = "<"
    GreaterThanOrEqualTo = ">="
    LesserThanOrEqualTo = "<="
    EqualTo = "="
