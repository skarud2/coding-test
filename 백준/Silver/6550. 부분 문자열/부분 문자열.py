#2025-07-01
import sys
from collections import deque

result=[]

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
        s,t=line.rsplit()
        
        s=deque(list(s))
        t=deque(list(t))
        find=s.copy()
        queue=[]

        while find:
            target=find.popleft()
            
            for _ in range(len(t)):
                if t.popleft()==target:
                    queue.append(target)
                    break
        

        if queue==list(s):
            result.append("Yes")
        else:
            result.append("No")
    
    except EOFError: break
        
for i in result: print(i)