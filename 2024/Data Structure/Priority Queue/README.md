# 우선 순위 큐 

## 1. 개념 및 기본 설명 

- 우선 순위 큐는 배열 기반으로도 구현될 수 있지만, 주로 완전 이진 트리를 기반으로 구현되며 이때 enqueue와 dequeue의 시간 복잡도는 모두 O(logn)이다
- 따라서 **Heap이라는 자료 구조는 완전이진트리 형태를 하고 있으며**, 이걸로 우선순위 큐를 만들 수 있다

### 최대힙 VS 최대힙 
![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/7c7743e4-91b9-4d60-a2d9-b75fd2053ed0)

- 최대 힙(max heap)은 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리이다.
- 최소 힙(min heap)은 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리이다.


## 2. 시간복잡도 
- 우선순위 가장 높은 데이터 찾기 : O(1)
- heapify : O(logN)
    ![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/ae761461-208d-4146-a9ec-824be76f2b49)

- 추가 연산 : O(logN) - 트리의 최대 높이만큼 동작하기 때문에 
  ![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/ebc0fa5c-7903-40d9-855a-5ff615823a96)
- 삭제 연산 : O(logN) - 트리의 최대 높이만큼 동작하기 때문에 
  ![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/3ebe40eb-cfb7-4f4e-ad78-fcce3396454c)




## 3. 사용 조건 



## 4. 사용되는 자료구조 및 알고리즘 & 기본 코드



## 5. 문제 유형 
### 우선 순위 큐로 중앙값 구하기 
- 1655.py 문제
- **왼쪽 힙은 최대 힙으로 정렬하고, 오른쪽 힙은 최소 힙으로 정렬하면 왼쪽 힙의 첫번째 요소는 항상 중앙값이 된다.**
  -  leftheap이 최대힙인 이유는, leftheap에 들어간 수는 중간값보다 작은 수이다. 그 작은 수 중에서 가장 큰 값이 중간값이 되기 때문에 루트가 최댓값이 되는 최대 힙을 사용한다.
반대로 rightheap같은 경우 중간 값보다 큰 수 들이 들어가고 그 수 중에서 가장 작은 수가 중간 값 다음에 나와야 하기 때문에 가장 작은 수가 루트가 되는 최소 힙을 사용한다.
    - 이때 왼쪽 힙의 첫번째 요소는 최대 힙에서 가장 큰 값이다.
    - 마찬가지로 오른쪽 힙의 첫번째 요소는 최소 힙에서 가장 작은 값
  - 과정
    1. 왼쪽 힙과 오른쪽 힙의 길이가 같으면 (요소 * -1) 을 왼쪽 힙에 삽입한다.
       - 그렇지 않으면 오른쪽 힙에 삽입한다.
    2. 왼쪽 힙과 오른쪽 힙에 요소가 존재하고, 왼쪽 힙의 (첫번째 요소* -1) 가 오른쪽 첫번째 요소보다 클 때
       - 왼쪽 힙의 첫번째 요소와 오른쪽 힙의 첫번째 요소를 바꿔준다. ( -1을 곱해준 뒤 바꿔준다. )
    왼쪽 힙의 (첫번째 요소 * -1)를 출력한다.

