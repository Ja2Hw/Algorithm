def solution(clothes):
    answer = 1
    only_type = [ clothes[i][1] for i in range(len(clothes))]
    set_type = list(set(only_type))
#   if len(set_type) == 1:
#       return len(clothes)
    for s in set_type:
        answer *= (only_type.count(s) + 1)
        
    return answer-1
'''
    stk = []
    tmp = 0
    answer = 0
    only_type = [ clothes[i][1] for i in range(len(clothes))]
    c_type = list(set(only_type))
    print(c_type)
    
    if len(c_type) > 1:
        tmp = 1
        for i in range(len(c_type)):
            if i > 2:
                tmp *= ( only_type.count(c_type[i]) + 1 )
                print(tmp)
            else :
                tmp *= only_type.count(c_type[i])
                print(tmp)
            
    answer += (len(clothes) + tmp)
    
    return answer

'''