from engine import Value

a = Value(2)
b = Value(1)

print("a:", a)
print("b:", b)

c = Value(a + b)
print("c:", c)

d = c - b
print("d:", d)
