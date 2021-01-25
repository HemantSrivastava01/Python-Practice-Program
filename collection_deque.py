from collections import deque

a = ['h', 'e', 'm', 'a', 'n', 't']
b = deque(a)
print(b)

b.appendleft('python')
print(b)

b.popleft()
print(b)
