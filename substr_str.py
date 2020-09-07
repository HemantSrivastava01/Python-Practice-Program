import re

# Take input from users
MyStr1 = input("enter first string : ")
MyStr2 = input("the word to be find : ")

# re.search() returns a Match object if there is a match anywhere in the string
if re.search(MyStr2, MyStr1):
    print("YES,string '{0}' is present in string '{1}' " .format(
        MyStr2, MyStr1))
else:
    print("NO,string '{0}' is not present in string {1} " .format(
        MyStr2, MyStr1))
