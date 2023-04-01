from collections import defaultdict

'''
[시간초과 해결]
1. 딕셔너리는 리스트보다 연산 속도가 훨씬 빠르다. 
2. for문 제거 : 기타 파이썬 메소드를 잘 사용하자
3. 형 변환은 생각보다 시간이 많이 잡아먹는다
'''


def solution(X, Y):
    table_x = defaultdict(int)
    table_y = defaultdict(int)

    for n in X:
        table_x[n] += 1

    for n in Y:
        table_y[n] += 1

    intersection = set(table_x.keys()) & set(table_y.keys())

    strings = ""
    for n in list(intersection):
        count = min(table_x[n], table_y[n])
        strings += n * count

    result = sorted(strings, reverse = True)

    if not result:
        return "-1"

    if result[0] == "0":
        return "0"

    return "".join(result)
