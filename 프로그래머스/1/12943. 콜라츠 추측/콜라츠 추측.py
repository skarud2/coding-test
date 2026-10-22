def solution(num):
    if num==1:
        return 0
    count=0
    result=0
    bf_num=num
    while(result!=1):
        result=(bf_num//2) if (bf_num%2==0) else (bf_num*3+1)
        count+=1
        bf_num=result
        if count>500:
            return -1
    
    return count
