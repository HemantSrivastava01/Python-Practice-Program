l1 = [10, 20, 30, 40, 50]


def my_itr():
    index = 0
    while index < len(l1):
        print(l1[index])
        index += 1
    else:
        print("no element left in the list")


def my_pro():
    pr = 1
    index = 0
    while index < len(l1):
        pr *= l1[index]
        index += 1
    print("Product is: {}".format(pr))


my_itr()
my_pro()
