def solution(cards):
    flags=[False for n in range(len(cards))]
    open_box_len_list=[]
    
    for i in range(len(cards)):
        open_box_len=0
        n=i+1
        while(1):
            if(flags[n-1]==True):
                break
            flags[n-1]=True
            open_box_len+=1
            n=cards[n-1]
        open_box_len_list.append(open_box_len)  
                   
    if (len(open_box_len_list)<2):
        return 0
    
    
    open_box_len_list.sort(reverse=True)
    
    
    answer = open_box_len_list[0]*open_box_len_list[1]
    return answer