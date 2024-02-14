import sys
from collections import deque

input = sys.stdin.readline
month = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
N = int(input())
flist = []

# start month/day, end month/day
def solve(t, sm, sd, em, ed, cnt):
    front = []
    end = []
    no = []

    for opt in t:
        if opt[0] < sm or (opt[0] == sm and opt[1] <= sd):
            front.append(opt)
        elif opt[2] > em or (opt[2] == em and opt[3] > ed):
            # 지는 날은 당일이랑 겹치게 하면 안돼
            end.append(opt)
        else:
            no.append(opt)

    # 지금 시간 구성도 sm, sd, em, ed, time 순서
    # 시작일과 겹치는 seg 중에 지는 일이 가장 늦은
    # 종료일과 겹치는 seg 중에 피는 일이 가장 앞선
    # 시작일, 종료일이 모두 겹치면 front, end 둘다 들어감

    front.sort(key=lambda x: (-x[2], -x[3]))
    end.sort(key=lambda x: (x[0], x[1]))

    #print(front, 'front')
    #print(end, 'end')
    #print(no, 'no')

    # front와 end에 0번 인덱스 이후 애들은
    # 무조건 0번과 같거나 그보다 못한 선택임에 유의
    # 남은 seg의 시작일을 front[0]의 끝점,
    # 남은 seg의 끝나는 날을 end[0]의 시작점으로 바꿔서 반복

    if len(front) == 0:
        print(0)  # 잇는게 불가능한 경우
        sys.exit()

    elif len(end) == 0:
        # end 배열이 없고 front[0]로 못끝나면 불가능
        # 왜냐하면 내가 시작점 겹치는걸 front에 먼저 넣어줘서 시작~끝 다 겹치는 구간이 front에 있을 가능성
        if front[0][2] > em or (front[0][2] == em and front[0][3] > ed):
            print(cnt+1)
        else:
            print(0)
        sys.exit()

    elif front[0][2] > em or (front[0][2] == em and front[0][3] > ed):
        # front, end 모두 있지만, front에서 한 번에 끝나는 경우
        print(cnt + 1)
        sys.exit()

    elif front[0][2] > end[0][0] or (front[0][2] == end[0][0] and front[0][3] >= end[0][1]):
        # 앞, 뒤 하나씩 연결해서 연결이 완성되는 경우
        print(cnt + 2)
        sys.exit()

    else:  # 둘 다 연결했는데 안됐을 때 no 배열으로 다시 돌리기
        sm, sd = front[0][2], front[0][3]
        if end[0][1] == 1:
            em = end[0][0]-1
            ed = month[em]
        else:
            em, ed = end[0][0], end[0][1]-1 #부등호 처리 귀찮아서 그냥 하루 앞으로 돌리기

        if len(no) != 0:
            solve(no, sm, sd, em, ed, cnt + 2)
        else:
            #만약 더이상 연결할 seg가 없으면 불가능
            print(0)
            sys.exit()


if N == 1:  # edge case
    t = list(map(int, input().split()))
    res = True

    if t[0] > 3 or (t[0] == 3 and t[1] > 1):
        res = False
    if t[2] < 11 or (t[2] == 11 and t[3] <= 30):
        res = False
    print(1 if res else 0)

else:
    for _ in range(N):
        t = list(map(int, input().split()))
        flist.append(t)
    solve(flist, 3, 1, 11, 30, 0)