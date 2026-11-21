class Query:
    conditions: list = []

    @staticmethod
    def on(column: str, value: any):
        pass


if __name__ == "__main__":
    Query.on("name", "Taha Shieenavaz")
