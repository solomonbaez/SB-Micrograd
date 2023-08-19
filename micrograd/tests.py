from engine import Value

########## Value methods ##########
a = Value(2)
b = Value(1)

print("a:", a)
print("b:", b)

c = a + b
print("c:", c)
print("c - children:", c._prv)
print("c - operation:", c._op)

d = c * b
print("d:", d)
print("d - children:", d._prv)
print("d - operation:", d._op)
