def check(string):
    stack = []
    for char in string : 
        if char =='(':
            stack.append(char)
        else : 
            if stack:
                stack.pop()
            else : 
                return "NO"

    if stack:
        return "NO"
    else: 
        return "YES"


K = int(input())

for i in range(K):
    string = input()
    print(check(string))
