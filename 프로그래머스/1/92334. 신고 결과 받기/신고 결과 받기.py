#딕셔너리 관련 함수
# keys() : 키만 반환
# items() : 키와 값을 모두 반환
# values() : 값만 반환

def solution(id_list, report, k):
    report = list(set(report))
    give_list = {name:[] for name in id_list} #어떤 이가 신고한 사람들 리스트
    take_count = {name:0 for name in id_list} #어떤 이가 신고당한 수 리스트
    bad = [] #정지 먹은 사람 목록
    mail = {name:0 for name in id_list} #메일 보낼 사람 리스트
    
    for r in report: #신고한 사람, 신고당한 사람 리스트 분리 작업
        d = r.split()
        give = d[0] #신고한 사람
        take = d[1] #신고당한 사람
        if give in give_list:
            give_list[give].append(take) #어떤 사람을 신고했는지 추가
        if take in take_count:
            take_count[take] += 1 #얼마나 신고당했는지 횟수 추가
        
    
    for name, cnt in take_count.items(): #신고 당한 횟수
        if cnt >= k: #k번 이상 신고 당한 사람을 정지 목록에 추가
            bad.append(name)
    
    for n in bad: #정지 먹은 사람들
        for name, take in give_list.items(): 
            if n in take: #정지 먹은 사람을 신고한 사람
                mail[name] += 1 #메일 횟수 추가
                
    return list(mail.values())
    
    
    
    
    
    '''
    report_ls = []
    report = list(set(report)) #중복 제거
    bad = []
    bad_cnt = 0
    for r in report:
        report_ls.append(r.split())
    print(report_ls)
    
    for i in id_list:
        for ls in report_ls:
            if ls[1] == i:
                bad_cnt += 1
                if k <= bad_cnt: #신고 받은 수
                    bad.append(i)
                    bad = list(set(bad))
            if i             
                    
    for b in bad:           
                    
    answer = []
    return bad
    '''