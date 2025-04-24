#250424
import sys
input=sys.stdin.readline

#서로 다른 버스 개수:n, 영식 터미널 도착 시간:t
n, t = map(int,input().split())
#버스 시작 시간:s, 버스 간격:i, 버스 대수:c
#영식이가 기다려야 하는 시간 출력
# (영식이 도착 후)가장 빠른 출발 버스 시간-영식 터미널 도착 시간
# 버스 출발 시간=버스 시작 시간+버스 간격


min_wait=float('inf')
for _ in range(n):
    s, i, c =map(int,input().split())
    for k in range(c):
        bus=s+i*k
        if bus>=t:
            min_wait=min(min_wait, bus-t)
            break

if min_wait==float('inf'):
    print(-1)
else:
    print(min_wait)

        