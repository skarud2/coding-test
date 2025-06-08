#2025-06-08
import sys
input=sys.stdin.readline
from collections import deque

#집 있는 곳:1, 집 없는 곳:0
n=int(input().rstrip())
mmap=deque([])
for i in range(n):
    mmap.append(list(map(int,list(input().rstrip()))))
       

#시계방향
dx=[0,1,0,-1]
dy=[1,0,-1,0]

queue=deque([])
visited=[[False]*n for _ in range(n)]
total=0
num=[]
number=0

for i in range(n):
    for j in range(n):
        if mmap[i][j]==1 and not visited[i][j]:
            queue.append((i,j))
            visited[i][j]=True
            number+=1
            total+=1
            
            while queue:
                x,y=queue.popleft()
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if 0<=nx<n and 0<=ny<n and mmap[nx][ny]==1 and not visited[nx][ny]:
                        queue.append((nx,ny))
                        visited[nx][ny]=True
                        number+=1
            
            num.append(number)
        number=0
        

num.sort()
print(total)
for _ in range(total):
    print(num[_])
