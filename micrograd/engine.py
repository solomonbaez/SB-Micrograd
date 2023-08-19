class Value:
    # wrapper
    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"Value(data={self.data})"

    def __add__(self, operand) -> int:
        result = self.data + operand.data

        return result

    def __sub__(self, operand) -> int:
        result = self.data - operand.data

        return result

    def __mul__(self, operand) -> int:
        result = self.data * operand.data

        return result

    def __div__(self, operand) -> int:
        result = self.data / operand.data

        return result
