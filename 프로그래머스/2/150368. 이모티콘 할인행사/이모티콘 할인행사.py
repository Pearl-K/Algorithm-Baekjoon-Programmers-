from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    answer = [0, 0]
    
    for dis_comb in product(discounts, repeat=len(emoticons)):
        plus_member = 0
        total_price = 0
        
        for user in users: # 비율, 가격
            max_port, max_price = user
            user_price = 0
            
            for i, dis_port in enumerate(dis_comb):
                if dis_port >= max_port:
                    user_price += emoticons[i]*(100-dis_port)//100
            
            if user_price >= max_price:
                plus_member += 1
            else:
                total_price += user_price
        
        if plus_member > answer[0]:
            answer = [plus_member, total_price]
        elif plus_member == answer[0]:
            answer[1] = max(answer[1], total_price)
        
    return answer