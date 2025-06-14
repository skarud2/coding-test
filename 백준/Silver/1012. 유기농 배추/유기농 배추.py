#2025-06-14
import sys
input=sys.stdin.readline
from collections import deque

t=int(input().rstrip())
result=[]

for _ in range(t):
    m, n, k=map(int, input().rsplit())

    graph=[[0]*m for _ in range(n)]
    visited=[[False]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().rsplit())
        graph[y][x]=1

    def bfs(graph, x,y, visited):
        queue=deque([(x,y)])
        visited[y][x]=True
        while queue:
            u,v=queue.popleft()
            dx=[0,1,0,-1]
            dy=[1,0,-1,0]
            for q in range(4):
                nx=u+dx[q]
                ny=v+dy[q]
                if 0<=nx<m and 0<=ny<n and graph[ny][nx]==1 and not visited[ny][nx]:
                    queue.append((nx,ny))
                    visited[ny][nx]=True

    cnt=0
    for y in range(n):
        for x in range(m):
            if graph[y][x]==1 and not visited[y][x]:
                bfs(graph, x,y, visited)
                cnt+=1
                   
    result.append(cnt)


for r in result:
    print(r) 