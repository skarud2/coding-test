#2025-06-13
import sys
input=sys.stdin.readline

n, m=map(int, input().rsplit())
graph=[[] for _ in range(n+1)]
for i in range(m):
    u, v=map(int, input().rsplit())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, v, visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
cnt=0        
visited=[False for _ in range(n+1)]
for j in range(1, n+1):
    if not visited[j]:
        dfs(graph, j, visited)
        cnt+=1
    
print(cnt)