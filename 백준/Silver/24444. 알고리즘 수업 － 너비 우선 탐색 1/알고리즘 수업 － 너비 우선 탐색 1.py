#25-08-04,5
import sys
input=sys.stdin.readline
from collections import deque

n,m,start=map(int,input().rsplit())

graph=[[] for _ in range(n+1)]  #1부터 시작
for _ in range(m):
    u,v=map(int, input().rsplit())
    graph[u].append(v)
    graph[v].append(u)

visited=[0 for _ in range(n+1)]
for i in graph: #인접 영역 오름차순 방문
    i.sort()

queue=deque([])
def dfs(s):
    order=1
    queue.append(s)
    visited[s]=order
    while queue:
        u=queue.popleft()
        for i in graph[u]:
            if not visited[i]:
                order+=1
                queue.append(i)
                visited[i]=order

dfs(start)

for i in visited[1:]:
    print(i)