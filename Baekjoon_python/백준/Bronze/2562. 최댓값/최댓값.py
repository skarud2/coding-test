#2025-05-22
import sys
input=sys.stdin.readline

num=[]
for _ in range(9):
    num.append(int(input().rstrip()))

result=max(num)
print(result)
print(num.index(result)+1)