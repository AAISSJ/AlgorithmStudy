import math 

a, b = map(int, input().split())
n,m = map(int, input().split())

ja = a*m + b*n 
mo = b*m 

gcd = math.gcd(ja, mo)

print(ja//gcd, mo//gcd)

