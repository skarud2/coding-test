#20250402
#수식의 개수 t 입력
t=int(input())
#t개의 수식 입력 (a개의 !, 정수n, b개의 !)
#정수:0 또는 1 / !: 0개 이상
testNum=[]
intIndex=[]
intNum=[]   
for j in range(t):
    tmp=list(input())
    temp=[]
    for i in range(len(tmp)):
        if tmp[i].isdigit():
            temp.append(int(tmp[i]))
            intIndex.append(i)  #정수 인덱스 저장
            intNum.append(int(tmp[i]))  #정수 저장
        else:
            temp.append(tmp[i])
        i+=1
    testNum.append(temp)
    j+=1

#! 있을 때 수식 계산 우선순위
    #1. 팩토리얼
       #0,1 뒤에 !이 한 개 이상 붙으면 결과는 항상 1
    #2. 논리 반전(not)
#! 없을 때 => 양의 정수는 항상 true => 1 출력
result=[] #최종값이 들어가는 리스트
i=j=0
for i in range(t):
    num=intNum[i]
    if '!' in testNum[i]:
        if num==0: #주어진 정수가 0일 때
            if intIndex[i]==(len(testNum[i])-1):   #팩토리얼 없는 경우. 논리 반전만 있는 경우
                if intIndex[i]%2==1: #not의 개수가 홀수 => 결과는 정수 반대로
                    result.append('1')
                else:   #not의 개수가 짝수 => 결과는 똑같이
                    result.append('0')
            else:   
                num=1   #팩토리얼 있는 경우 =>결과는 무조건 1
                if intIndex[i]%2==1: #not의 개수가 홀수 => 결과는 정수 반대로
                    result.append('0')
                else:
                    result.append('1') 

        else: #주어진 정수가 1일 때
            if intIndex[i]==len(testNum[i]):   #팩토리얼 없는 경우. 논리 반전만 있는 경우
                    result.append('0')
            else:   #팩토리얼 있는 경우 =>결과는 무조건 1
                if intIndex[i]%2==1: #not의 개수가 홀수 => 결과는 정수 반대로
                    result.append('0')
                else:
                    result.append('1') 
        
    
    else:
        if intNum[i]==0:
            result.append('0')
        else:
            result.append('1')
    i+=1

print('\n'.join(result))