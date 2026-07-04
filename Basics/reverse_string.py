str = input("Give the string you want to reverse: ")
str_length = len(str)
reversed_string=""
for char in range(0, str_length):
    reversed_string = str[char]+reversed_string
print(reversed_string)