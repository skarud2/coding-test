def solution(n):
    # 짝수일 때는 2로 나누고
    # 홀수일 때는 3 * x + 1로 바꾸
    # 언젠가는 반드시 x가 1이 되는지
    # 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열
    answer = []
    answer.append(n)
    while(n!=1):
        if(n%2==0):
            n/=2
        else:
            n*=3
            n+=1
        answer.append(n)  
    
    return answer