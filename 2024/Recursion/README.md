
⛅ 재귀의 시간복잡도 = 재귀 함수 호출 수 x (재귀 함수 하나당) 시간복잡도


## 코테 사용 방법

- 재귀는 추후 `그래프 탐색`, `트리` , `dp` 등 주요 자료구조와 알고리즘에 접목되기에 중요하다
- 직접 사용하는 걸로는 `분할정복` 알고리즘도 있다!

## 재귀의 구성요소 2가지

- `Recurrence Relation`⇒ 점화식
    - problem과 subproblem의 관계식을 가리킴
- `Base Case`
    - 정의: 더 이상 재귀 호출을 하지 않아도 계산값을 반환할 수 있는 상황(조건)
    - 모든 입력이 최종적으로 Base Case를 이용해서 문제를 해결할 수 있어야 함
    - Base Case가 무조건 있어야만, 재귀함수의 무한 루프를 방지할 수 있음
