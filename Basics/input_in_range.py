#Take the input unless the user gives between 1 and 10

while True:
    number = int(input("Enter a number b/w 1 and 10: "))
    if(number >1 and number <10):
        print("The number is: ", number)
        break
    else:
        print("Invalid Number, Try Again!")
