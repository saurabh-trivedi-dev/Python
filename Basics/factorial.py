num = int(input("Give the number to print the factorial: "))
factorial=1

while(num>1):
    factorial = factorial*num
    num-=1

print(factorial)