N = int(input())

def recursion(s, l, r, cnt):
    if l >= r: 
        return 1, cnt
    elif s[l] != s[r]: 
        return 0, cnt
    else: # l<r and s[l] == s[r]
      return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)


for i in range(N):
    return_num, call_num = isPalindrome(input())
    print(return_num, call_num)
