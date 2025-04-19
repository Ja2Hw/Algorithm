import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    sm = input().strip()
    if sm == 'Algorithm':
        print(204)
    elif sm == 'DataAnalysis':
        print(207)
    elif sm == 'ArtificialIntelligence':
        print(302)
    elif sm == 'CyberSecurity':
        print('B101')
    elif sm == 'Network':
        print(303)
    elif sm == 'Startup':
        print(501)
    elif sm == 'TestStrategy':
        print(105)
        