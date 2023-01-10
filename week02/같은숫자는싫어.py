def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.   
    last = None 
    for num in arr : 
        if last != num  :
            last = num
            answer.append(num)
    return answer
