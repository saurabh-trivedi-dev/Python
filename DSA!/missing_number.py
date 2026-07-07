

def missing_number(arr, n):

    total = 0
    whole = 0

    for i in arr:
        total = total+i
    
    for j in range(0, n+1):
        whole = whole+j

    return whole-total


arr = [0,4,2,1]
n=4

result = missing_number(arr, n)
print(result)

