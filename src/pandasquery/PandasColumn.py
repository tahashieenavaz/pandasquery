from .PandasQueryColumn import PandasQueryColumn


class PandasColumn(PandasQueryColumn):
    def __init__(self, name: str):
        self.name = name
