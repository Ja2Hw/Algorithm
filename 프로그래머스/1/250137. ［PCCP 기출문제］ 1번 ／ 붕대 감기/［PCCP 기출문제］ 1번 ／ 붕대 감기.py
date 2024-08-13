# bandage = [붕대 감기 시전 시간 t, 1초당 회복량 x, 추가 회복량 y]
# health = 최대 체력
# attacks = [[공격하는 시간, 피해량], ...] (2차원 배열)

def solution(bandage, health, attacks): #[시전 시간, 초당 회복량, 추가회복량]
    heal_stk = 1
    time = 1
    max_health = health
    last_time = attacks[-1][0]
    while time <= last_time: #시간의 흐름
        
        if time == attacks[0][0]: #공격 당했을 때
            health -= attacks[0][1]
            attacks.pop(0)
            heal_stk = 1
            if health <= 0:
                return -1
            
        else: #공격 안 당했을 때 (회복 타이밍)
            if heal_stk == bandage[0]: #연속 회복 성공
                health += (bandage[1] + bandage[2])
                heal_stk = 1
                
            else: #연속 회복 아닐 때
                health += bandage[1]
                heal_stk += 1    
                
            if health > max_health: #최대 체력
                    health = max_health
        
        time += 1
        
    return health