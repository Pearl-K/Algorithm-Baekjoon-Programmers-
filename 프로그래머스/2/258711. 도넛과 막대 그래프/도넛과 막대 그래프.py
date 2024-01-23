from collections import defaultdict

def solution(edges):
    res = [0]*(4)
    e_len = len(edges)
    graph = defaultdict(lambda: [0, 0])
    
    for u, v in edges:
        graph[u][0] += 1
        graph[v][1] += 1
    
    for node, cnt in graph.items():
        give = cnt[0]
        take = cnt[1]
        if give >= 2 and take == 0:
            res[0] = node
        elif give == 0 and take >= 1:
            res[2] += 1
        elif give >= 2 and take >= 2:
            res[3] += 1
    total_node = graph[res[0]][0]
    res[1] = total_node - (res[2]+res[3])
    return res