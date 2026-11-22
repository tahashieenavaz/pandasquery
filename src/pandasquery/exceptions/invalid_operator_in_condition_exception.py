class InvalidOperatorInConditionException(Exception):
    def __init__(self, operator):
        super().__init__(f"Invalid operator found in conditions. {operator}")
