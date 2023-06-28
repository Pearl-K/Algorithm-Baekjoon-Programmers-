# 문제 접근법 구상하기
# 1. backtraking? No, 수열 시작과 끝의 인덱스를 찾기가 어려워짐
# 2. DP 누적합을 이용한 DP, 연속된 비내림차순 수열이므로 사용 가능 -> but 
# 3. 이분 탐색과 투 포인터 이용

def solution(sequence, k):
    answers = []
    sum = 0
    left = 0
    right = -1
    
    while True:
        if sum < k:
            right += 1
            if right >= len(sequence):
                break
            sum += sequence[right]
        else:
            sum -= sequence[left]
            if left >= len(sequence):
                break
            left += 1
        if sum == k:
            answers.append([left, right])
            
    #인덱스 차이가 가장 작은 걸로 answers 리스트 sorting
    answers.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answers[0]