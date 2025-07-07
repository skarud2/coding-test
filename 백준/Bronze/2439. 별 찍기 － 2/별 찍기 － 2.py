#2025-07-07
import sys
input=sys.stdin.readline

n=int(input().rstrip())
star=[]

for i in range(1,n+1):
    print(' '*(n-i) + '*'*i)