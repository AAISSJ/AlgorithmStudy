# Lowest Common Ancestor (LCA, 최소 공통 조상)
![img1 daumcdn](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/744093ec-f580-47b6-b359-48a73bb61c69)

- 기본 로직
  1. 각 노드의 깊이 구하기 & 부모 노드 구하기 by dfs (루트 노드부터 시작하여 깊이(depth)를 구하는 함수)
  2. 부모(i=0)보다 높은 전체 조상(1<=i<LOG) 관계를 설정하는 함수
      - 아래의 점화식 형태를 가짐
        - parent[j][i] = parent[parent[j][i - 1]][i - 1] 
  3. A와 B의 최소 공통 조상을 찾는 함수
      - 1 ) 항상 b가 더 깊도록 설정
      - 2 ) a와 b의 깊이가 동일해주도록 설정
      - 3-1 ) 깊이가 같을 때 둘이 동일하다면? ( 11438번 문제의 예제 1의 2,6의 경우 )
      - 3-2 ) (깊이가 같지만 둘이 동일하지 않은 경우) 위로 올라가면서 공통 조상 찾기
        -  위(루트)를 향해 거슬러 올라가기
        - a와 b의 부모가 같아지면 갱신하지 않음
