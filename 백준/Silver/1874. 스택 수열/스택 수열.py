#20250404
# c을 1부터 n까지 하나씩 올려가며 stack에 push
# stack[-1]이 목표 숫자(num)와 같으면 pop

import sys

n=int(sys.stdin.readline())
purpose=[]
stack=[]
result=[]

for i in range(n):
    num=int(sys.stdin.readline())   
    purpose.append(num)


pushNum=1
for i in range(n):
    while pushNum<=purpose[i]:
        stack.append(pushNum)
        result.append('+')
        pushNum+=1

    
    if stack[-1]==purpose[i]:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        sys.exit()

print('\n'.join(result))