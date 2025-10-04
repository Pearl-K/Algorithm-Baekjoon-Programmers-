def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}
    
    for name in callings:
        cur_idx = rank[name]

        front = players[cur_idx - 1]
        players[cur_idx - 1], players[cur_idx] = players[cur_idx], players[cur_idx - 1]
        
        rank[name] -= 1
        rank[front] += 1
    
    return players
