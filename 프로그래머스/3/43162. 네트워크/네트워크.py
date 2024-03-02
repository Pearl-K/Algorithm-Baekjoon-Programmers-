import sys
sys.setrecursionlimit(10**6)

def find_p(me, parent):
    if parent[me] != me:
        return find_p(parent[me], parent)
    else:
        return me

def union_p(a, b, parent):
    pa = find_p(a, parent)
    pb = find_p(b, parent)
    
    if pa > pb: #a가 항상 더 작게 유지
        pa, pb = pb, pa
    
    parent[pb] = pa
    
    
def solution(N, computers):
    #컴퓨터 개수 N, 연결 정보가 0 ro 1로 N^2 형태로 주어짐
    
    parent = [i for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            elif computers[i][j] and parent[i] != parent[j]:
                union_p(i, j, parent)
    
    res = set()
    for i in range(len(parent)):
        res.add(find_p(parent[i], parent))
    
    ans = len(res)
    return ans