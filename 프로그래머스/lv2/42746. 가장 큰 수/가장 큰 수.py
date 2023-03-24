def solution(num):
    N = len(num)
    num_str = list(map(str, num))
    
    num_str.sort (key=lambda x: x*3, reverse=True)
    ans = int(''.join(num_str))
    return str(ans)