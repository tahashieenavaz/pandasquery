class UnknownBinderException(Exception):
    def __init__(self):
        super().__init__(
            "Unknown condition type was passed. Condition binder must be in {AND, OR}."
        )
