#25-08-16
import sys
input=sys.stdin.readline
from collections import deque

n=int(input().rstrip())

#나이트 이동 칸
d=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
result=[]

def bfs(sr,sc,v):
    queue.append((sr,sc,v))
    visited[sr][sc]=True
    while queue:
        r,c,v=queue.popleft()
        if r==tr and c==tc:
            return v
        for i in range(8):
            nx=r+d[i][0]
            ny=c+d[i][1]
            if 0<=nx<m and 0<=ny<m and not visited[nx][ny]:   
                queue.append((nx,ny,v+1))
                visited[nx][ny]=True
            
for _ in range(n):
    m=int(input().rstrip())
    fr, fc=map(int, input().rsplit())    #현재 좌표
    tr, tc=map(int, input().rsplit())    #도착지 좌표
    visited=[[False] *m for _ in range(m)]
    queue=deque([])
    result.append(bfs(fr,fc,0))
    
for j in range(n):
    print(result[j])
    