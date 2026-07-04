input_str = input("Give the staring to search first non-repeating character: ")

for char in input_str:
    print(char)
    if (input_str.count(char) == 1):
        print("The first non-repeating character in the string is: ", char)
        break
