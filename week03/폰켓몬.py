def solution(nums):
    answer = 0
    
    cnt=len(list(set(nums)))
        
    if len(nums)/2 <= cnt :
        answer=len(nums)/2
    else :
        answer=cnt
    
    return answer
