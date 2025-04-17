#250417
#최소점수, 최대점수

import sys
input=sys.stdin.readline

#수강한 과목 수:n, 실제 반영 과목 수:m, 공개한 과목 수:k
n,m,k=map(int,input().split())

#수강한 과목과 점수 저장
dic={}
for _ in range(n):
    key,value=input().split()
    dic[key]=value
#점수 순으로 정렬
sorted_dic=dict(sorted(dic.items(), key=lambda x:int(x[1])))
#공개한 과목 input

openSum=0
for _ in range(k):
    open_sub=input().rstrip()
    openSum+=int(sorted_dic[open_sub])
    sorted_dic.pop(open_sub)

#(실제 반영 과목 수 - 공개한 과목 수)만큼 더하기(최대, 최소)
min, max=openSum, openSum
#과목 점수만 따로 리스트 생성
list_dic=list(sorted_dic.values())
for p in range(m-k):
    min+=int(list_dic[p])
    max+=int(list_dic[len(list_dic)-p-1])

print(min, max)