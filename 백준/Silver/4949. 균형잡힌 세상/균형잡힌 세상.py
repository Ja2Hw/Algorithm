import sys

stk = []

while True:
    line = sys.stdin.readline().rstrip()
    
    stk = []
    
    if line == '.':
        break
    
    for l in line:
        if l=='(' or l=='[': # 여는 괄호가 오면 스택에 추가
            stk.append(l)
        elif l==')': # ) 인 경우
            if len(stk)!=0 and stk[-1]=='(': # 스택이 비어있지 않고, 마지막 요소가 ( 이면 pop
                stk.pop()
            else: # 스택이 비어있거나 짝이 맞지 않으면 스택에 )을 추가하고 break
                stk.append(l)
                break
        elif l==']': # ] 인 경우
            if len(stk)!=0 and stk[-1]=='[': # stack이 비어있지 않고, 마지막 요소가 [ 이면 pop
                stk.pop()
            else: # 스택이 비어있거나 짝이 맞지 않으면 스택에 ]을 추가하고 break
                stk.append(l)
                break

    if len(stk)==0: # 스택이 비어있으면 모든 괄호들의 균형이 맞으므로 yes 출력
        print('yes')
    else: # 스택이 비어있지 않으면 괄호들의 균형이 맞지 않는 것이므로 no 출력
        print('no')