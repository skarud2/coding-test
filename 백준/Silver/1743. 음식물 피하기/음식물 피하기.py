#2025-06-09
import sys
input=sys.stdin.readline

n, m, k=map(int, input().rsplit())

mmap=[[0]*m for _ in range(n)]
for _ in range(k):
    x,y=map(int, input().rsplit())
    mmap[x-1][y-1]=1
                
visited=[[False]*m for _ in range(n)]
stack=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

size_arr=[]

for i in range(n):
    for j in range(m):
        if mmap[i][j]==1 and not visited[i][j]:
            stack.append((i,j))
            visited[i][j]=True
            size=1
            
            while stack:
                x,y=stack.pop()
                    
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    
                    if 0<=nx<n and 0<=ny<m and mmap[nx][ny]==1 and not visited[nx][ny]:
                        stack.append([nx,ny])
                        visited[nx][ny]=True
                        size+=1
            size_arr.append(size)

print(max(size_arr))