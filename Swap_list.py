import math
# To get Entry from User-->
NumArr = []
n = int(input("Enter the list size : "))
print("\n")
for i in range(0, n):
    print("Enter number at location", i, " : ")
    item = int(input())
    NumArr.append(item)
print("User Entered List is : ", NumArr)

# function for swapping


def swapList(list, f, s):
    first = list.pop(f)
    last = list.pop(s-1)
    list.insert(f, last)
    list.insert(s, first)
    return list


f = int(input("enter the 1st number to be swapped : "))
s = int(input("enter the 2nd number to be swapped : "))
print("Reversed list is : ", swapList(NumArr, f-1, s-1))
