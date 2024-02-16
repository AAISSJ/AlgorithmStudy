

# 정수론


## 에라토스테네스의 체 
- n 이하의 모든 소수 구함 - 시간 복잡도 O(NlogN)
- 코드 외워두도록 하자
```
def make_primes(num): 
    count_dic = {i:True for i in range(0, num+1)}
    count_dic[0]=False
    count_dic[1]=False
    for i in range(2, num+1):
        if count_dic[i]: # True라면
            for j in range(i*i, num+1, i): # 요부분 주목!
                count_dic[j]=False
    return count_dic
```
