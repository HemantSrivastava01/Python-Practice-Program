import math
# To get Entry from User-->
NumArr = []
n = int(input("Enter the list size : "))
print("\n")
for i in range(0, n):
    print("Enter number at location", i, " : ")
    item = int(input())
    NumArr.append(item)
print("User Entered Array is : ", NumArr)

# Function for finding greatest element-->


def largest(NumArr, g):
    max = NumArr[0]
    for i in range(1, g):
        if NumArr[i] > max:
            max = NumArr[i]
    return max


g = len(NumArr)
Ans = largest(NumArr, n)
print("Largest element in given array : ", Ans)
# To print sum of the array-->
Ans = sum(NumArr)
print("Sum of the Array is : ", Ans)
