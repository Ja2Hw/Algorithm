# 27162 Yacht Dice
# 실버 3

import sys

def compute_score(dice, category_idx):
    if 0 <= category_idx <= 5:  # Ones to Sixes
        target = category_idx + 1
        return sum(d for d in dice if d == target)
    
    elif category_idx == 6:  # Four of a Kind
        for value in range(1, 7):
            if dice.count(value) >= 4:
                return value * 4
        return 0
    
    elif category_idx == 7:  # Full House
        counts = {}
        for d in dice:
            counts[d] = counts.get(d, 0) + 1
        
        values = list(counts.values())
        if len(counts) == 2 and (3 in values and 2 in values):
            return sum(dice)
        return 0
    
    elif category_idx == 8:  # Little Straight
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        return 0
    
    elif category_idx == 9:  # Big Straight
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        return 0
    
    elif category_idx == 10:  # Yacht
        if len(set(dice)) == 1:
            return 50
        return 0
    
    elif category_idx == 11:  # Choice
        return sum(dice)
    
    return 0

def solve():
    # 선택 가능한 족보 읽기
    available = input().strip()
    available_categories = [i for i in range(12) if available[i] == 'Y']
    
    # 고정된 주사위 읽기
    fixed_dice = list(map(int, input().strip().split()))
    
    max_score = 0
    
    # 남은 두 주사위의 모든 경우의 수 시뮬레이션 (1-6, 1-6)
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            current_dice = fixed_dice.copy() + [d1, d2]
            
            # 각 선택 가능한 족보에 대한 점수 계산
            for category in available_categories:
                score = compute_score(current_dice, category)
                max_score = max(max_score, score)
    
    return max_score

print(solve())