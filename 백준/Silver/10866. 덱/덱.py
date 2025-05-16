#2025-05-16
import sys
input=sys.stdin.readline
from collections import deque


n=int(input().rstrip())
commend=[]
for i in range(n):
    commend.append(list(input().rsplit()))
    
dq= deque([]) 
for i in range(n):
    if len(commend[i])==2:
        if commend[i][0]=="push_front":
            dq.appendleft(commend[i][1])
        else:
            dq.append(commend[i][1])
    elif commend[i][0]=="pop_front":
        if len(dq)<=0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif commend[i][0]=="pop_back":
        if len(dq)<=0:
            print(-1)
        else:
            print(dq[-1])
            dq.pop()
    elif commend[i][0]=="size":
        print(len(dq))
    elif commend[i][0]=="empty":
        if len(dq)<=0:
            print(1)
        else:
            print(0)
    elif commend[i][0]=="front":
        if len(dq)<=0:
            print(-1)
        else:
            print(dq[0])
    elif commend[i][0]=="back":
        if len(dq)<=0:
            print(-1)
        else:
            print(dq[-1])