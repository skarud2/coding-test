def solution(arr):
    arr=set(arr)
    result=[]
    for i in arr:
        count=0
        bf_i=i
        while(True):
            if i%2==0:  #짝수
                if i>=50:
                    i=(i//2) 
            else:       #홀수
                if i<50:       
                    i=(i*2+1)
            if bf_i==i:
                    break
            bf_i=i
            count+=1
        
        result.append(count)
               
    return max(result) 