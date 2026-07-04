x = int(input("Please give a number you want the table of: "))

for i in range(1,11):
    if(i==5):
        continue
    print(x, "X", i, "=", x*i)