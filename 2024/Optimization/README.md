# Optimization

- 동적 프로그래밍(Dynamic Programming, DP), 분할 정복(Divide and Conquer), 그리디(Greedy) 알고리즘은 모두 문제를 효율적으로 해결하기 위한 알고리즘 

<br>

| 알고리즘 | Divide and Conquer | Dynamic Programming | Greedy |
| --- | --- | --- | --- |
| **정의**  | non-overlapping한 문제를 작은 문제로 쪼개어 해결하는데 non-overlapping | overlapping substructure를 갖는 문제를 해결한다. | 각 단계에서의 최적의 선택을 통해 해결한다. |
| **접근 방법** | top-down 접근 | top-down, bottom-up 접근 |  |
| **사용되는 개념** | 재귀 함수를 사용한다. | 재귀적 관계(점화식)를 이용한다.(점화식) | 반복문을 사용한다. |
| **답을 구하는 방식 (중복 처리)** | call stack을 통해 답을 구한다.- 중복 처리 없음, 분할하여 독립적 해결	 | look-up-table, 즉 행렬에 반복적인 구조의 solution을 저장해 놓는 방식으로 답을 구한다. | solution set에 단계별 답을 추가하는 방식으로 답을 구한다.- 중복 처리 없음 |
| **기본 코드 구조** | 분할 - 정복 - 병합 | 점화식 도출 - look-up-table에 결과 저장 - 나중에 다시 꺼내씀 | 단계별 최적의 답을 선택 - 조건에 부합하는지 확인 - 마지막에 전체조건에 부합하는지 확인 |
| **활용 알고리즘** | 이분탐색, 퀵소트, 머지소트 | 최적화 이분탐색, 이항계수 구하디, 플로이드-와샬 | 크루스칼, 프림, 다익스트라, 벨만-포드 |
| 문제를 쪼갤 때 작아진 문제의 크기 | 지수적으로 줄어든다  | 선형적으로 줄어든다  |  |
