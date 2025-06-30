#20250401
#1 ≤ N ≤ 100개의 문자열 중 소문자, 대문자, 숫자, 공백 개수 구하기
import sys

printResults=[]

for line in sys.stdin:
    line = line.rstrip('\n')  # 개행 문자 제거
    if not line:
        break

    lowercase=uppercase=num=space=0

    for ch in line:
        if ch.islower():  #만약 소문자면 lowercase 1증가  
            lowercase+=1
        elif ch.isupper():  #만약 대문자면 uppercase 1증가
            uppercase+=1
        elif ch.isdecimal():    #만약 숫자면 num 1증가
            num+=1  
        else:   #만약 공백이면 space 1증가
            space+=1

    printResults.append(f"{lowercase} {uppercase} {num} {space}") #결과 리스트에 저장

for result in printResults:
    print(result)
