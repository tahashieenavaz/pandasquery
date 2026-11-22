class EmptyConditionsException(Exception):
    def __init__(self):
        super().__init__(
            "Please start the conditions using `where` method and continue using auxiliaries such as `andWhere` and `orWhere`."
        )
