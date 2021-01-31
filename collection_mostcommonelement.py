from collections import Counter
st = input("Give any random word")
print("given string: "+st)
print("most common word of the given string: ")
print(Counter(st).most_common(len(st)))
