#2025-06-29,30
import sys
input=sys.stdin.readline
from collections import deque

r,c =map(int, input().rsplit())
mmap=[]*r
for i in range(r):
    mmap.append(list(input().rstrip()))

map_dict={
    'D':(0,0,0),
    'S':(0,0,0),
    '*':[],
    'X':[]
}

for i in range(r):
    for j in range(c):
        if mmap[i][j]=='D':
            map_dict['D']=(i,j,0)
        elif mmap[i][j]=='S':
            map_dict['S']=(i,j,0)
        elif mmap[i][j]=='*':   #물 여러개 가능
            map_dict['*'].append((i,j,0))
        elif mmap[i][j]=='X': #돌 여러개 가능
            map_dict['X'].append((i,j,0))

#1. 물 먼저 퍼짐
dist_water=[[-1]*c for _ in range(r)]

queue=deque([])
queue.extend(map_dict['*'])
while queue:
    ro,co,dist=queue.popleft()
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    for i in range(4):
        nr=ro+dr[i]
        nc=co+dc[i]
        if 0<=nr<r and 0<=nc<c:
            if mmap[nr][nc]=='.' and dist_water[nr][nc]==-1:
                    queue.append((nr,nc,dist+1))
                    dist_water[nr][nc]=dist+1

#2. 고슴도치 움직임
dist_dochi=[[-1]*c for _ in range(r)]
queue.append(map_dict['S'])
while queue:
    ro,co,dist=queue.popleft()
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    for i in range(4):
        nr=ro+dr[i]
        nc=co+dc[i]
        if 0<=nr<r and 0<=nc<c:
            if dist_water[nr][nc]>dist+1 or dist_water[nr][nc]==-1:
                if dist_dochi[nr][nc]==-1: #고슴도치가 먼저 도착
                    if mmap[nr][nc]=='.' :
                        queue.append((nr,nc,dist+1))
                        dist_dochi[nr][nc]=dist+1
                    elif mmap[nr][nc]=='D':
                        print(dist+1)
                        exit(0)
            
print("KAKTUS") #비버의 굴로 이동할 수 없는 경우