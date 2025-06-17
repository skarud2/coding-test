#2025-06-17
import sys
input=sys.stdin.readline
from collections import deque
n=int(input().rstrip())
m=int(input().rstrip())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    u,v=map(int, input().rsplit())
    graph[u].append(v)
    graph[v].append(u)

visited=[False for _ in range(n+1)]
queue=deque([])
cnt=0

def bfs(start):
    queue.append(start)
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                global cnt
                cnt+=1
                
bfs(1)
print(cnt)