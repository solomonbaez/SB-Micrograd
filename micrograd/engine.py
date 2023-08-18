class Value:
    # wrapper
    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"Value(data={self.data})"