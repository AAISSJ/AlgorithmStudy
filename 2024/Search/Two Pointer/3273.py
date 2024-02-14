N = int(input())
arr = list(map(int, input().split()))
x= int(input())

left=0 
right=len(arr)-1
cnt =0 
arr.sort()

while left<right:
    if arr[left]+arr[right]==x:
        cnt+=1
        left+=1
    elif arr[left]+arr[right]<x:
        left +=1 
    else:
        right-=1

print(cnt)

