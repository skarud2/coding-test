#2025-05-29
import sys
input=sys.stdin.readline
from collections import deque

n, m=map(int,input().rsplit())
arr=deque([])
for i in range(n):
    arr.append(i+1)
    
target=deque(map(int,list(input().rsplit())))

    
count=0
while len(target)!=0:
    if target[0]==arr[0]:
        arr.popleft()
        target.popleft()
    else:
        target_idx=0
        for i in range(len(arr)):
            if target[0]==arr[i]:
                target_idx=i
                break
            
        if int(len(arr)/2)+1<=target_idx:
            while (target[0]!=arr[0]):
                arr.appendleft(arr.pop())
                count+=1
        else:
            while (target[0]!=arr[0]):
                arr.append(arr.popleft())
                count+=1

            

print(count)
        