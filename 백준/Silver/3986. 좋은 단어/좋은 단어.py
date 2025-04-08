import sys
input=sys.stdin.readline

#단어 수
n=int(input().rstrip())

good=0
for _ in range(n):
    stack=[]
    tmp=list(input().rstrip())
    for i in tmp: 
        if not len(stack):  #스택이 비어있을 경우
            stack.append(i)
        elif stack[-1]==i:  #같은 문자가 top에 있는 경우
            stack.pop()
        else:   #다른 문자가 top에 있는 경우
            stack.append(i)

    #stack에 남아 있는 게 없으면 => 좋은 문자
    if not len(stack):
        good+=1

print(good)
    