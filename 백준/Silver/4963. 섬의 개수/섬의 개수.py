#2025-06-07
import sys
input=sys.stdin.readline
from collections import deque

result=[]
while 1:
    cnt=0
    w,h=map(int, input().rsplit())   #w:열(col), h:행(row)
    
    if w==0 and h==0:
        break
    
    mmap=deque([])
    for i in range(h):
        mmap.append(list(map(int, input().rsplit())))
    
    visited=[[False]*w for _ in range(h)]
    
    #상하좌우대각선이 연결되어 있으면 하나로 본다.
    d_row=[0,1,0,-1,1,1,-1,-1]   
    d_col=[1,0,-1,0,1,-1,-1,1]   
    queue=deque([])
    
    for r in range(h):
        for c in range(w):
            if not visited[r][c] and mmap[r][c]==1:
                visited[r][c]=True
                cnt+=1
                queue.append((r,c))
                while queue:
                    row,col = queue.popleft()
                    for k in range(8):
                        n_col = col + d_col[k]
                        n_row = row + d_row[k]
                        if 0 <= n_col < w and 0 <= n_row < h and mmap[n_row][n_col] == 1 and not visited[n_row][n_col]:
                            visited[n_row][n_col] = True
                            queue.append((n_row, n_col))

                
    result.append(cnt)
            
print(*result,sep='\n')