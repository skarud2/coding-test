#2025-05-30
import sys
input=sys.stdin.readline
from collections import deque

x, y=map(int, input().rsplit())
box=[]

for _ in range(y):
    box.append(list(map(int, input().rsplit())))

one=deque([])
empty=0
zero=0
for i in range(y):
    for j in range(x):
        if box[i][j]==1:
            one.append((i,j,0))
        elif box[i][j]==-1:
            empty+=1
        else:
            zero+=1


if len(one)==x*y:   #다 1일 때 (이미 다 익은 상태)
    print(0)
    exit()
    
if zero==x*y or empty==x*y:   #다 -1일 때
    print(-1)
    exit()

while one:
    a,b,d=one.popleft()
    if a>0 and box[a-1][b]==0:   #상
        box[a-1][b]=1
        one.append((a-1,b,d+1))
    if a<y-1 and box[a+1][b]==0:   #하
        box[a+1][b]=1
        one.append((a+1,b,d+1))
    if b>0 and box[a][b-1]==0:  #좌
        box[a][b-1]=1
        one.append((a,b-1,d+1))
    if b<x-1 and box[a][b+1]==0:   #우
        box[a][b+1]=1
        one.append((a,b+1,d+1))
        
for i in range(y):
    for j in range(x):
        if box[i][j]==0:   #0이 남아있을 경우
            print(-1)
            exit()
    
print(d)
