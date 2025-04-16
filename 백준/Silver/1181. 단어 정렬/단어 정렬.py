#250416
import sys
input=sys.stdin.readline

#단어 개수 입력
num=int(input().rstrip())

words=set()

for _ in range(num):
    words.add(input().rstrip())

result=sorted(words, key=lambda x: (len(x), x))

for i in result:
    print(i)

