#2025-05-17
import sys
input=sys.stdin.readline
import heapq

n=int(input().rstrip())

arr=[]
for n in range(n):
    tmp=int(input().rstrip())
    arr.append(tmp)

arr_abs=[]
arr_heapq=[]

for i in range(n+1):
    if arr[i]!=0:   #0이 아닐 경우
        if arr[i]<0:    #음수일 경우
            heapq.heappush(arr_heapq,arr[i])
            heapq.heappush(arr_abs, abs(arr[i]))    #절댓값 저장
        else:   #양수일 경우
            heapq.heappush(arr_heapq,arr[i])
            heapq.heappush(arr_abs, arr[i])
    else:   #0일 경우
        if len(arr_heapq)==0:
            print(0)
        elif (-1)*arr_abs[0] in arr_heapq:    #-절댓값이 원래 리스트(arr_heap)에 있는 경우
            target=arr_heapq.index((-1)*arr_abs[0])
            print((-1)*arr_abs[0])
            heapq.heappop(arr_abs)
            arr_heapq.pop(target)
        else:   #절댓값이 양수일 경우
            print(arr_abs[0])
            target=arr_heapq.index(arr_abs[0])
            heapq.heappop(arr_abs)
            arr_heapq.pop(target)
        
            

        