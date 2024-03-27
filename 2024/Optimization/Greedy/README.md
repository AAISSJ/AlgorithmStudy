
# Greedy

## 1. 개념 및 기본 원리 
- 정의
  - 지금 가장 최적인 답을 근시안적으로 택하는 알고리즘
  - 관찰을 통해 탐색 범위를 줄이는 알고리즘

<br>

- 이상적인 풀이 전략
  1. 관찰을 통해 탐색 범위를 줄이는 방법을 고안한다
  2. 탐색 범위를 줄여도 올바른 결과를 낸다는 사실을 수학적으로 증명한다
  3. 구현해서 문제를 통과한다
**=> 단, 실제 코테 현장에서는 수학적인 증명을 할 수 없기 때문에 ...**

- 현실적인 풀이 전략 & 절망편
  1. 관찰을 통해 탐색 범위를 줄이는 방법을 고안한다
  2. 탐색 범위를 줄여도 올바른 결과를 낸다는 "강한 믿음을 가진다"
  3. "믿음을 가지고" 구현해서 문제를 통과한다
**=> 하지만 구현 또는 접근 방법의 문제로 틀릴 수도 있다 ㅎㅎ**

<br>

- 코딩테스트에서의 추천전략
  1. **거의 똑같은 문제를 풀어봤거나 간단한 문제여서 나의 그리디 풀이를 100% 확신한다**
      - 짜서 제출해보고 틀리면 빠르게 손절
  2. **100% 확신은 없지만 맞는 것 같은 그리디 풀이를 찾았다**
      - 일단은 넘어가고 다른 문제를 풀 게 없거나 종료가 20~40분 남은 시점에 코딩 시작 

<br>

### 예제 (BOJ 1931 회의실 배정)
![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/4ff2e55c-bfce-485d-b5e2-439cea11517c)
![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/ed6b642e-8b8b-42a3-a58a-f18be9c3ac22)

- 이 증명에서도 귀류법이 쓰입니다. 명제를 거짓이라고 가정하면 지금 이 상황에서 회의 A 말고 다른 회의를 택했을 때 더 많은 회의를 배정할 수 있는 경우가 있습니다. 설명의 편의를 위해 택한 다른 회의를 B라고 하겠습니다.

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/aca48516-eb60-4ce2-8b41-19668468bed5)

- 회의 B를 회의 A로 변경해도 스케쥴에는 아무런 문제가 없습니다. 회의 A는 남아있는 회의 중에서 가장 먼저 끝나는 회의이니 당연히 회의 A가 회의 B보다 먼저 끝나기 때문입니다. 그러면 회의 A 말고 회의 B를 선택했을 때 더 많은 회의를 배정할 수 있다고 했는데 해당 스케쥴에서 회의 B를 A로 변경하는 방법을 생각해보면 회의 A를 택했을 때 적어도 회의 B를 택했을 때 만큼의 회의는 진행할 수 있습니다 그렇기 때문에 모순을 찾았고 결론적으로 처음의 명제가 맞아서 우리의 그리디 알고리즘이 올바르다는걸 증명해냈습니다.




## 2. 시간 복잡도 




## 3. 사용 조건 



## 4. 사용되는 자료구조 및 알고리즘 & 기본 코드 



## 5. 문제 유형


## 6. Reference
- [바킹독의 실전 알고리즘] https://www.youtube.com/watch?v=De0Qg-2O80c




 