"""
if a duplicate is found in list, break the loop and print the duplicate
count in list for every elemnt if count is >1, break and print duplicate
"""

list1 = ["banana", "mango", "orange", "kiwi", "cherry", "litchi", "kiwi"]


# for element in list1:
#     if(list1.count(element)>1):
#         print("Duplicate is:", element)
#         break

# else:
#     print("No Duplicate Found!!")


unique_elements =set()

for element in list1:
    if element in unique_elements:
        print("Duplicate: ", element)
        break
    unique_elements.add(element)

else:
    print("No Duplicate Found!!")




