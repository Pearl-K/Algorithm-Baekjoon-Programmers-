import sys
import heapq as hq
#idea_힙을 두 개 만들면 안되나?
N = int(sys.stdin.readline())
plus = [] #양수 저장
minus = [] #음수 저장
for i in range(N):
    num = int(sys.stdin.readline())
    if num < 0:
        hq.heappush(minus, -num) #절댓값 최소 힙 만들고자 양수로 저장
    elif num == 0:
        if plus and minus:
            if plus[0] == minus[0]:
                print(-hq.heappop(minus))
            elif plus[0] > minus[0]:
                print(-hq.heappop(minus))
            elif plus[0] < minus[0]:
                print(hq.heappop(plus))
        elif plus:
            print(hq.heappop(plus))
        elif minus:
            print(-hq.heappop(minus))
        else:
            print(0)
    else:#case: num > 0
        hq.heappush(plus, num)