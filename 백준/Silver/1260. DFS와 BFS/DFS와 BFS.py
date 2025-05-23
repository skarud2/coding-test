#2025-05-23
import sys
input=sys.stdin.readline
from collections import deque

def dfs(graph, start):
    visited=[False for _ in range(len(graph))]
    stack=[start] #방문 전 노드들
    result=[]
    while stack:
        v=stack.pop()
        if not visited[v]:
            visited[v]=True
            result.append(v)
            for i in reversed(graph[v]):
                if not visited[i]:  #아직 방문 안했으면(visited[i]==false)
                    stack.append(i)
    return result

def bfs(graph, start):
    visited=[False for _ in range(len(graph))]
    queue=deque([start])
    result=[]
    while queue: 
        v=queue.popleft()
        visited[v]=True
        result.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    return result
                
    
n, m, s=map(int,input().rstrip().rsplit())   #n정점개수, m간선개수, s시작정점번호
edgeList=[]
for _ in range(m):
    edgeList.append(list(map(int, input().rstrip().rsplit())))

#간선->인접리스트 변환
graph=[[] for _ in range(n+1)]
for u, v in edgeList:
    graph[u].append(v)
    graph[v].append(u)

#방문 가능한 정점이 여러 개일 경우=> 번호가 작은 것부터 먼저 방문
for i in range(len(graph)):
    graph[i].sort()

print(' '.join(map(str,dfs(graph, s))))
print(' '.join(map(str,bfs(graph, s))))