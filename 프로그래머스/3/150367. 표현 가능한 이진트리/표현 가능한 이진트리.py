import math

def dfs(tree_str):
    if len(tree_str) == 1:
        return True
    
    mid = len(tree_str)//2
    root = tree_str[mid]
    left = tree_str[:mid]
    right = tree_str[mid+1:]
    
    if root == '0' and ('1' in left+right):
        return False
    
    return dfs(left) and dfs(right)

def solution(numbers):
    # 모든 서브 트리에 대하여 전위 순회하는 순서
    # 관찰을 해보니, 모든 subtree의 root는 반드시 존재해야한다.
    # 그러면 root가 0일 때 subtree 노드가 하나라도 1인 순간 fail
    answer = []
    
    for num in numbers:
        binary = bin(num)[2:]
        full_len = 2**math.ceil(math.log2(len(binary)+1))-1
        binary = binary.zfill(full_len)
        answer.append(1 if dfs(binary) else 0)
    return answer