num = int(input("Enter a number : "))

isDivisible = False
i = 2
while i < num:
    if num % i == 0:
        isDivisible = True
        print("{} is divisible by {}".format(num, i))
    i += 1
if isDivisible:
    print("{} is Not A Prime Number".format(num))
else:
    print("{} is A Prime Number".format(num))
