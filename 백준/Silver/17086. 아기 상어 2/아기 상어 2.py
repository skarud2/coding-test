#2025-06-18
import sys
input=sys.stdin.readline
from collections import deque

n, m=map(int, input().rsplit())
mmap=[[] for _ in range(n)]
for i in range(n):
    mmap[i].extend(map(int, input().rsplit()))

q=deque([])
dist=[[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mmap[i][j]==1:
            q.append((i,j))
            dist[i][j]=0
        
dx=[0,1,0,-1,1,1,-1,-1]
dy=[1,0,-1,0,1,-1,-1,1]

while q:
    x,y=q.popleft()
    for r in range(8):
        nx=x+dx[r]
        ny=y+dy[r]
        if 0<=nx<n and 0<=ny<m and dist[nx][ny]==-1:
            q.append((nx,ny))
            dist[nx][ny]=dist[x][y]+1        

max_dist=-1
for i in range(n):
    for j in range(m):
        if max_dist<dist[i][j]:
            max_dist=dist[i][j]
            
print(max_dist)  