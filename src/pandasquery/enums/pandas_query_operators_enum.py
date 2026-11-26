from enum import StrEnum


class PandasQueryOperatorsEnum(StrEnum):
    EqualTo = "="
    GreaterThan = ">"
    LesserThan = "<"
    GreaterThanOrEqualTo = ">="
    LesserThanOrEqualTo = "<="
    StartsWith = "startswith"
    StartsWithSymbol = "^"
    EndsWith = "endswith"
    EndsWithSymbol = "$"
