#2025-06-26
import sys
input=sys.stdin.readline
from collections import deque

n, k=map(int, input().rsplit())

queue=deque([(n,0)])
dist=[100001 for _ in range(100001)]

if n==k:
    print(0)
    exit(0)
else:
    while queue:
        lo,cnt=queue.popleft()
        move=[lo*2, lo-1, lo+1]
        for i in move:
            if 0<=i<=100000:
                if i==lo*2 and dist[i]>cnt:
                    queue.append((i,cnt))
                    dist[i]=cnt
                elif dist[i]>cnt+1:
                    queue.append((i,cnt+1))
                    dist[i]=cnt+1   
    print(dist[k])