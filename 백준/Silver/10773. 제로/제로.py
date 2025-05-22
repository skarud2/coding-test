#2025-05-22
import sys
input=sys.stdin.readline

k=int(input().rstrip())
arr=[]
for i in range(k):
    num=int(input().rstrip())
    if num==0:
        arr.pop()
    else:
        arr.append(num) 

if len(arr)!=0: 
    num=0
    for j in arr:
        num+=j
    print(num)
else:
    print(0)
