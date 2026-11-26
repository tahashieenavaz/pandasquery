from enum import StrEnum


class PandasQueryOperatorsEnum(StrEnum):
    GreaterThan = ">"
    LesserThan = "<"
    GreaterThanOrEqualTo = ">="
    LesserThanOrEqualTo = "<="
    EqualTo = "="
    StartsWith = "startswith"
    StartsWithSymbol = "$"
