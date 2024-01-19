N = int(input())


num = 666
cnt = 1
while 1:
    if '666' in str(num):
        cnt += 1
        if cnt == n:
            print(num)
            break
    num += 1
