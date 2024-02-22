from heapq import *
import sys
input = sys.stdin.readline 


V,E = map(int, input().split())


###################################################################
# 1. 크루스칼 - sort + Union Find -> 얘가 더 효율적임 

parent = [i for i in range(V+1)]
arr = []
for _ in range(E):
    A, B, C = map(int, input().split())
    arr.append((C,A,B))

arr.sort()

def find(a):
    if parent[a]==a:
        return a
    else: 
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a_root = find(a)
    b_root = find(b)
    parent[a_root]=b_root


answer = 0 
for weight, a, b in arr:
    if find(a)!=find(b):
        union(a,b)
        answer+=weight
        
print(answer)
