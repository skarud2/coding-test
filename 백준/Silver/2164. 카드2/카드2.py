#2025-05-20

import sys
input=sys.stdin.readline
from collections import deque

n=int(input().rstrip())

number=deque()
for i in range(n):
    number.append(i+1)
    

while len(number)!=1:
    number.popleft()
    number.append(number.popleft())
    
print(''.join(map(str,number)))