#accept number or string and return multiplication


def multiply(p1, p2):
    return (p1*p2)

result1 = multiply(5,6)
print(result1)

result2 = multiply("a",6)
print(result2)

result3 = multiply(6,"a")
print(result3)


# TypeError: can't multiply sequence by non-int of type 'str'
result4 = multiply("a","a")
print(result4)