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


def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i+1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


print("the element repeated in the list : ", Repeat(NumArr))
