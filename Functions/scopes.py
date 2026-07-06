#Scope and Closures in python

num1 = 99

def add(num):
    num2 = 1
    return num+num2

print(add(num1))




#It is a bad practice to do this
def multiply(num):
    global num1
    num1 = 3
    return num1**3

print(multiply(num1))




def func1(num1):
    def func2(num2):
        return num1*num2
    return func2

result = (func1(7))
finalresult = result(5)
print(finalresult)




def f1():
    x=88
    def f2():
        print(x)
    f2()
f1()