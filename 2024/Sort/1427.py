import sys 
input = sys.stdin.readline 

N = list(input())
N.sort(reverse=True)
print(''.join(N))

# N = int(input())
# str_N = str(N)

# tmp = [0] * 10
# for i in str_N:
#   tmp[int(i)]+=1


# for i in range(9, -1, -1):
#   if tmp[i]!=0: 
#     for j in range(tmp[i]):
#       print(i,end='')



