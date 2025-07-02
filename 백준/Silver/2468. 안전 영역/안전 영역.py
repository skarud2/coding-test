#2025-07-02
import sys
input=sys.stdin.readline
from collections import deque

n=int(input().rstrip())
graph=[list(map(int, input().rsplit())) for _ in range(n)]
queue=deque([])
direct=[(-1,0),(0,1),(1,0),(0,-1)]   #상, 우, 하, 좌
visited=[[False]*n for _ in range(n)]

def bfs(row, col, rain):
    queue.append((row, col))
    while queue:
        r,c=queue.popleft()
        visited[r][c]=True
        for dr,dc in direct:
            nr=r+dr
            nc=c+dc
            if 0<=nr<n and 0<=nc<n and graph[nr][nc]>rain and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc]=True

max_safe=max(map(max,graph))
r,cnt=0,0
result=[]
while max_safe>=r:       
    for i in range(n):
        for j in range(n):
            if graph[i][j]>r and not visited[i][j]:
                bfs(i,j,r)
                cnt+=1
    result.append(cnt)
    r+=1        
    cnt=0
    visited=[[False]*n for _ in range(n)]
    
print(max(result))