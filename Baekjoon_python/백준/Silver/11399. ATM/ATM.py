#20250507
import sys
input=sys.stdin.readline

n=int(input().rstrip())
p=[]
p.extend(map(int,input().split()))

sorted_p=sorted(p)
sum_p=[]
result=0
for i in range(n):
    sum=0
    for j in range(i+1):
        sum+=sorted_p[j]
    result+=sum

print(result)