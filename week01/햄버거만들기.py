def solution(ingredient):
    answer = 0
    st = []

    for i in ingredient:
        st.append(i)
        if len(st) >= 4:
            if st[-1] == 1 and st[-2] == 3 and st[-3] == 2 and st[-4] == 1:
                st.pop()
                st.pop()
                st.pop()
                st.pop()
                answer+=1

    return answer
