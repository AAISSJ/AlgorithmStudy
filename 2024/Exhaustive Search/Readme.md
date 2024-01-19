
# 알고리즘 푸는 순서 
- Step 1. 문제 이해하기 
- Step 2. 접근 방법 
- Step 3. 코드 설계
- Step 4. 코드 구현


- `Step 1. 문제 이해하기`  → ⭐️
    1. input, output 확인 
        - input 값의 특징 (정수인가? 값 크기의 범위는? 마이너스도 되는건가? 소수인가? 자료형은 문자열인가? 등등)
        - output 값의 특징 (내가 어떤 값을 변환해줘야 하는지, 정해진 형식대로 반환하려면 어떻게 구현할지)
    2. input size N 확인 
        - 시간복잡도를 계산하기 위한 input size N 또는 M이 무엇인지 확인하기
    3. 제약조건 확인
        - 시간 복잡도 제한이 있는지 확인
        - 내가 선택할 수 있는 알고리즘이 무엇이 있는지
    4. 예상할 수 있는 오류 파악 
        - 상황을 가정하면서 예상할 수 있는 오류를 파악한다
        - 입력값의 범위, stack overflow 등등
- `Step 2. 접근 방법` → ⭐️
    1. 직관적으로 생각하기 
        - 보통 **완전 탐색**으로 시작
        - 문제 상황을 단순화하여 생각하기
        - 문제 상황을 극한화하여 생각하기
    2. 자료 구조와 알고리즘 활용 
        - `Step 1` 에서 파악한 내용을 토대로 어떤 자료 구조를 사용하는 게 가장 적합한지 결정
        - 대놓고 특정 자료구조와 알고리즘을 묻는 문제도 많음
        - 자료 구조에 따라 선택할 수 있는 알고리즘을 문제에 적용
    3. 메모리 사용 
        - 시간 복잡도를 줄이기 위해 메모리를 사용하는 방법
        - 대표적으로 해시 테이블
- `Step 3. 코드 설계`
- `Step 4. 코드 구현`



# Brute-force 
- 모든 경우를 다 탐색한다
- 할 수 있는 가장 기초적인 방법
- `Step 1. 문제 이해하기` 단계에서 input을 확인하는 것 중요
  - 10^8 넘어가지 않으면 완전 탐색으로 풀어도 ㅇㅋ