def cantor(start_index, segment_length):
    if segment_length == 1:
        return

    middle_start = start_index + segment_length // 3
    middle_end = start_index + (segment_length // 3) * 2

    for i in range(middle_start, middle_end):
        cantor_set[i] = ' '

    cantor(start_index, segment_length // 3)
    cantor(start_index + (segment_length // 3) * 2, segment_length // 3)

while True:
    try:
        N = int(input())
        cantor_set = ['-'] * (3**N)
        cantor(0, 3**N)
        print(''.join(cantor_set))
    except:
        break
