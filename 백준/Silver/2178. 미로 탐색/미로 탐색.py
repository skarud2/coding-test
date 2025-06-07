#2025-06-07
import sys
input=sys.stdin.readline
from collections import deque

#도착위치 (n,m)
n,m=map(int, input().split())

maze=[]
for _ in range(n):  
    maze.append(list(map(int,list(input().strip()))))

#상하좌우
dx=[0,0,-1,1]
dy=[1,-1,0,0]

canMove=deque([(0,0,1)])
visited=[[False]*m for _ in range(n)]
visited[0][0]=True

while canMove:
    x,y,dist=canMove.popleft()
    
    if x==n-1 and y==m-1:
        print(dist)
        break
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1 and not visited[nx][ny]:
            visited[nx][ny]=True
            canMove.append((nx,ny,dist+1))