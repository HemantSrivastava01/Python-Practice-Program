import math
from collections import Counter
# To get Entry from User-->
NumArr = []
n = int(input("Enter the list size : "))
print("\n")
for i in range(0, n):
    print("Enter number at location", i, " : ")
    item = int(input())
    NumArr.append(item)
print("User Entered List is : ", NumArr)
x = int(input("Enter the element to be find occurence of : "))
d = Counter(NumArr)
print('{} has occurred {} times'.format(x, d[x]))
