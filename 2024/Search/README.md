# Search 

<img width="1132" alt="image" src="https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/86589428-ab30-47f4-a02f-608c75ed433b">

- 좌측의 Search 문제만을 다룬다
- 되도록이면 Dictionary로 풀자
  - 메모리가 많이 들긴 하지만, 가장 쉽고 빠르다 


## 1. 해시 탐색 
- O(N)의 시간 복잡도를 가짐 

## 2. 이분 탐색(이진 탐색, Binary Search)
- 만약 해시 탐색으로도 해결되지 않는 입력 범위라면? -> "이분 탐색"
  - **O(logN)**의 시간 복잡도를 가짐
- 단, 데이터가 정렬되어있어야 함 
- 중요한 특징 중 하나 : **lower bound & upper bound**

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/2c82b3c6-9b48-4039-baf8-bd4bce696379)

- [이분 탐색(Binary Search) 헷갈리지 않게 구현하기 ](https://www.acmicpc.net/blog/view/109)https://www.acmicpc.net/blog/view/109

  
## 3. Two Pointer 알고리즘
- 완전 탐색 문제 O(N^2)를 개선할 때 적용할 수 있음  
  - O(N)의 시간 복잡도
- **Two Pointer 적용하는 문제 특징**
  - **연속된 구간의 원소들을 처리하거나 (e.g. 부분합 문제)**
  - **정렬된 배열에서 무언가를 구할 때**
- 이분 탐색과는 달리, 정렬되어 있지 않아도 됨
- 문제 종류
  - 두 개 다 왼쪽에서 시작/각각 왼쪽, 오른쪽에서 / 다른 배열
  - 일반적으로는 O(N) / 정렬 후 Two Pointer O(NlogN) 
