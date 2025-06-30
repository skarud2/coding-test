#2025-05-21
import sys
input=sys.stdin.readline
import ast
from collections import deque

t=int(input().rstrip())
result=[]
for _ in range(t):
    p=list(input().rstrip())    #수행할 함수
    n=int(input().rstrip())   #배열 원소 개수
    arr=ast.literal_eval(input().rstrip())  
    reverseF=False
    p=deque(p)
    arr=deque(arr)
    while True:
        if p[0]=='R':   #R
            reverseF= not reverseF
            p.popleft()
        else:   #D
            if len(arr)==0:
                result.append("error")
                break
            else:
                if reverseF:
                    arr.pop()
                else:
                    arr.popleft()
                p.popleft()

            
        if len(p)==0:
            if reverseF==True:
                arr.reverse()
            result.append(arr)
            break
        

for k in result:
    if k=='error':
        print(k)
    else:
        print("["+','.join(map(str, k))+"]")
