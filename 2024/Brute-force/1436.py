N = int(input())


num = 666
cnt = 1
while True : 
    if '666' in str(num) and cnt == N:
        print(num)
        break 
    elif '666' in str(num) and cnt != N:
        cnt +=1 
    num +=1 
