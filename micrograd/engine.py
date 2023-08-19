class Value:
    # wrapper
    def __init__(self, data, _children=(), _operation=""):
        self.data = data
        self._prv = set(_children)
        self._op = _operation

    def __repr__(self) -> str:
        return f"Value(data={self.data})"

    def __add__(self, operand) -> int:
        result = Value((self.data + operand.data), (self, operand), "+")

        return result

    def __sub__(self, operand) -> int:
        result = Value((self.data - operand.data), (self, operand), "-")

        return result

    def __mul__(self, operand) -> int:
        result = Value((self.data * operand.data), (self, operand), "*")

        return result

    def __div__(self, operand) -> int:
        result = Value((self.data / operand.data), (self, operand), "/")

        return result
