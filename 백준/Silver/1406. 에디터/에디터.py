#2025-05-17
import sys
input=sys.stdin.readline


left_stack=list(input().rstrip())
m=int(input().rstrip())
right_stack=[]
cmd=[]

for _ in range(m):
    cmd.append(list(input().rsplit()))

for i in range(m):
    if len(cmd[i])==2: #명령어 P
        left_stack.append(cmd[i][1])
    else:
        if cmd[i][0]=='L' and len(left_stack)!=0:
            right_stack.append(left_stack[-1])
            left_stack.pop()
        elif cmd[i][0]=='D'and len(right_stack)!=0:
            left_stack.append(right_stack[-1])
            right_stack.pop()
        elif cmd[i][0]=='B' and len(left_stack)!=0:
            left_stack.pop()

print(''.join(left_stack)+''.join(reversed(right_stack)))