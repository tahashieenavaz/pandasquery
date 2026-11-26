from .pandas_query_column import PandasQueryColumn


class PandasColumn(PandasQueryColumn):
    def __init__(self, column_name: str):
        self.name = column_name
