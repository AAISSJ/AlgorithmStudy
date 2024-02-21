# Union Find
-  Union Find : 두 노드가 같은 그래프에 속하는지 판별하는 알고리즘 (서로소 집합을 찾아내는 알고리즘)
  -  노드를 합치는 Union연산과 노드의 루트 노드를 찾는 Find연산으로 이루어짐
  -  init 연산
    ```
      arr = [i for i in range(N+1)]
    ```
  -  Union 연산
    ```
      def union(a,b):
        a_root = find(a)
        b_root = find(b)
        arr[a_root] = b_root
    ```
  -  Find 연산
    ```
      def find(a):
        if arr[a]==a :
            return a 
        else: 
            arr[a]=find(arr[a])
            return arr[a]
    ```
- **코테 활용**
  - Union Find를 활용하여 양방향 그래프에서 cycle 여부를 판단할 수 있다.
    - 각 간선의 두 노드의 루트 노드를 확인한다.
      - 루트노드가 서로 다르면 union 연산 실행
      - 루트노드가 서로 같으면 cycle 발생한 것
