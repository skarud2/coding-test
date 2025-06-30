#입력값: 검색 결과
#출력값: 패턴으로 뭘 쳐야 그 결과가 나오는지

def main():
    #파일 이름 개수; num<=50
    num=int(input())

    #파일 이름 입력; 이름 길이는 모두 같고 최대 50자
    #입력하면서 비교
    #한 글자씩 list에 담기
    #두 번째 이름의 인덱스와 비교
        #다르면 그 자리에 ?로 대치

    filename=list(input())

    for j in range(num-1):
        otherName=list(input())
        for i in range(len(filename)) :
            if filename[i]!=otherName[i]:
                filename[i]='?'

    print(''.join(filename))

if __name__ == "__main__":
    main()