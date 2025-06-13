#2025-06-13
import sys
input=sys.stdin.readline
from collections import deque

n, m= map(int, input().split())

info={}
want_pw=deque([])

for _ in range(n):
    site, pw=input().rsplit()
    info[site]=pw
    
for _ in range(m):
    want_pw.append(input().rstrip())

for i in range(m):
    
    print(info[want_pw.popleft()])