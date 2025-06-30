#2025-05-08
import sys
input=sys.stdin.readline

num=int(input().rstrip())
time=[]
for i in range(num):
    start, end = map(int,input().split())
    time.append((start,end))

# 끝나는 시간이 가장 빠른 순으로 정렬
# 끝나는 시간이 같을 경우에는 시작 시간이 빠른 순으로 정렬
time.sort(key=lambda x: (x[1],x[0]))

end_t=0
count=0

for start, end in time:
    if end_t<=start:
        end_t=end
        count+=1    

print(count)