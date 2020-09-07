def isPalindrome(s):
    rev = ''.join(reversed(s))
    if(s == rev):
        return True
    return False


s = input("Enter a string : ")
res = isPalindrome(s)
if (res):
    print("its a palindrome")
else:
    print("its not a palindrome")
