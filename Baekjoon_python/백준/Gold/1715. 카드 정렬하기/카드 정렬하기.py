#2025-05-11
import sys
import heapq
input=sys.stdin.readline

n=int(input().rstrip())
num=[]
for _ in range(n):
    num.append(int(input().rstrip()))

def sort_card(arr):
    heapq.heapify(arr)
    result=0
    while len(arr)>1:
        num1=heapq.heappop(arr)
        num2=heapq.heappop(arr)
        tmp=num1+num2
        heapq.heappush(arr,tmp)
        result+=tmp

    return result

print(sort_card(num))