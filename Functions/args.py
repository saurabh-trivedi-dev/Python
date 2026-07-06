
# *args (args come as a tuple) (they can be itarated if needed)

# we can also write *numbers or anything but it is not a good practice


def sum_all(*args):
    for i in args:
        print(i)
    return sum(args)

print(sum_all(1,2,3,4,5))