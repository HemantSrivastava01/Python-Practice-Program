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

even_count, odd_count = 0, 0
num = 0

while(num < len(NumArr)):
    if NumArr[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num += 1
print("even number in the list : ", even_count)
print("odd numbers in the list : ", odd_count)
