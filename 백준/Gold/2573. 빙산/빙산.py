#2025-07-05,07
import sys
input=sys.stdin.readline
from collections import deque, defaultdict


n, m= map(int, input().rsplit())
graph=[list(map(int, input().rsplit())) for _ in range(n)]
queue=deque([])
d=[(-1,0),(0,1),(1,0),(0,-1)] #(행, 열) 상,우,하,좌
ice={(i,j) for i in range(n) for j in range(m) if graph[i][j]>0} #빙산 높이가 0보다 큰 것만 저장


def bfs(row, col, value):
    queue.append((row, col, value))
    visited.add((row,col))
    
    while queue:
        r,c,v=queue.popleft()
        mel=0
        if v>0:
            for dr,dc in d:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m:
                    if graph[nr][nc]<=0:
                        mel+=1   #v의 주변 0 이하의 개수                    
                    else:
                        if (nr,nc) not in visited:
                            queue.append((nr,nc,graph[nr][nc]))
                            visited.add((nr,nc))   #방문한 좌표만 저장
        melt[(r,c)]=mel
        

                                  
cnt=0 
while True:
    visited=set() 
    block=0   #얼음 덩어리 개수
    melt=defaultdict(int)
    
    for (i,j) in ice:
        if (i,j) not in visited and graph[i][j]>0:
            block+=1
            bfs(i,j,graph[i][j])
        
    next_ice = set()
    for (i, j), val in melt.items():    #다음에 검사할 남아있는 빙산
        if graph[i][j] > 0:
            next_ice.add((i, j)) 
            
    for (ro, co), me in melt.items():     #빙산 높이 업데이트
        graph[ro][co]-=me
        
    if block>=2:
        print(cnt)
        exit(0)
    elif not next_ice:    #모든 빙산이 녹은 경우
        print(0)
        exit(0)
        
    cnt+=1   #빙산 분리되는 시간(년)
    ice=next_ice
        