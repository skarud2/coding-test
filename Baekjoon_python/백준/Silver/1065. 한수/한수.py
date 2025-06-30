#2025-05-08
import sys
input=sys.stdin.readline

def is_hs(num):
    str_n=str(num)
    if len(str_n)<3:
        return True
    else:
        d = int(str_n[1])-int(str_n[0])
        for i in range(1, len(str_n)-1):
            if d != int(str_n[i+1])-int(str_n[i]):
                return False
        return True 

#n은 1000이하 자연수
n=int(input().rstrip())

result=0
for i in range(1,n+1):
    if is_hs(i):
        result+=1

print(result)