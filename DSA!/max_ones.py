

def max_ones(arr):

    maximum_ones = 0
    current_ones = 0

    for element in arr:
        if (element == 1):
            current_ones+=1
        else:
            if(current_ones>maximum_ones):
                maximum_ones = current_ones
                current_ones = 0

    if(current_ones>maximum_ones):
                maximum_ones = current_ones

    return maximum_ones


arr = [1,1,1,1,1]

result = max_ones(arr)
print(result)

        