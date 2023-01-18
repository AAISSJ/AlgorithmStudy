def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
  
def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for i in range(0,len(participant)-1):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
        else :
            answer = participant[i+1]

    return answer
  
from collections import Counter

def solution(participant, completion):
    answer = ''
    p_dict = Counter(participant)
    c_dict = Counter(completion)

    for p_name in p_dict:
        if p_dict[p_name] != c_dict[p_name]: 
            answer = p_name

    return answer
