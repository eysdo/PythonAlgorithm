def use1(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b
def use2(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a,b
a = 23
b = 32
print(use1(a,b))
print(use2(a,b))