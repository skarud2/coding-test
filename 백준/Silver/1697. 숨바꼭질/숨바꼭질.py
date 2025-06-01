#2025-06-01
import sys
input=sys.stdin.readline
from collections import deque
#수빈위치:n, 동생위치:k
n,k=map(int, input().rsplit())

#(수빈현재위치, 시간)
subin=deque([(n,0)])
visited=[False]*100001

while subin:
    loc, time=subin.popleft()
    visited[loc]=True
    
    if loc==k:
        print(time)
        exit()
    
    for next_loc in [loc*2, loc+1, loc-1]:
        if 0<=next_loc<=100000 and not visited[next_loc]:
            subin.append((next_loc, time+1))
            visited[next_loc]=True
    
    
        

