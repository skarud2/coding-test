#2025-06-30
import sys
input=sys.stdin.readline

k,n=map(int,input().rsplit())
kList=[]
for _ in range(k):
    kList.append(int(input().rstrip()))
    
kList.sort()

start=0
end=kList[-1]
num=0
max_len=0

while start<=end:
    num=0
    mid=start+(end-start)//2
    
    for i in range(k):
        if mid!=0:
            temp=kList[i]//mid
            num+=temp
        
    if num<n:
        end=mid-1
    else:
        start=mid+1
        max_len=mid

if max_len==0:
    print(1)
    exit(0)
print(max_len)