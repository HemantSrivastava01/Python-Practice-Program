import math

start = int(input("enter first number : "))
end = int(input("enter second number : "))

for i in range(start,end):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
