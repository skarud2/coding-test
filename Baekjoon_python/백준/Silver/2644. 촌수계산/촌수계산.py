#2025-06-08
import sys
input=sys.stdin.readline


def dfs(graph, v, visited, t, cnt=0):
    visited[v]=True
    cnt+=1
    for i in graph[v]:
        if i==t:
            print(cnt)
            exit(0)
        if not visited[i]:
            dfs(graph, i, visited,t, cnt)



#전체 사람 수
n=int(input().rstrip())
#촌수를 계산해야 하는 두 사람 번호
a,b=map(int, input().rsplit())
#부모 자식들 간의 관계 개수
m=int(input().rstrip())
#부모자식간의 관계를 나타내는 번호
edges=[]
for _ in range(m):
    edges.append(list(map(int,input().rsplit())))

graph=[[] for _ in range(n+1)]

for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
    
visited=[False]*(n+1)

dfs(graph, a, visited, b)
print(-1)