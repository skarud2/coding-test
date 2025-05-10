#2025-05-10
import sys
input=sys.stdin.readline

n=int(input().rstrip())
aList=list(map(int,input().split()))
aList.sort()

m=int(input().rstrip())
mList=list(map(int,input().split()))

def binary_search(arr, target):
    start_idx=0
    end_idx=len(arr)-1

    while start_idx <= end_idx:
        mid_idx=(start_idx+end_idx)//2
        if target==arr[mid_idx]:
            return 1
        elif target>arr[mid_idx]:
            start_idx=mid_idx+1
        else:
            end_idx=mid_idx-1
    
    return 0

for target in mList:
    print(binary_search(aList,target))
