#2025-06-16
import sys
input=sys.stdin.readline
from collections import deque

n=int(input().rstrip())
graph=[[] for _ in range(n+1)]
for i in range(1,n):
    u, v= map(int,input().rsplit())
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(start):
    queue=deque([start])
    visited[start]=True

    while queue:
        now=queue.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt]=True
                queue.append(nxt)
                parent[nxt]=now

parent=[0]*(n+1)
visited=[False]*(n+1)
    
bfs(1)
    
for i in range(2,n+1):
    print(parent[i])
