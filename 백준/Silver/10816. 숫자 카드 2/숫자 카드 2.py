#2025-06-23
import sys
input= sys.stdin.readline
from collections import Counter
from collections import deque

n=int(input().rstrip())
sangeun=list(map(int, input().rsplit()))

m=int(input().rstrip())
card=deque(list(map(int, input().rsplit())))

dict=Counter(sangeun)
result=[]

while card:
    result.append(dict[card.popleft()])
    
for k in result:
    print(k, end=' ')