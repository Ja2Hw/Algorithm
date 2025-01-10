import sys

A = ['a', 'i', 'y', 'e', 'o', 'u']
B = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]

def transform(line):
    res = ''
    for l in line:
        up = l.isupper()  # 대문자인지 확인
        l = l.lower()  # 소문자로 변환

        if l in A:  # 모음
            ind = (A.index(l) + 3) % len(A)
            tmp = A[ind]
            res += tmp.upper() if up else tmp

        elif l in B:  # 자음
            ind = (B.index(l) + 10) % len(B)
            tmp = B[ind]
            res += tmp.upper() if up else tmp

        else:  # 점이나 공백 등
            res += l
    return res

# 입력을 한 번에 처리
input_data = sys.stdin.read().strip().splitlines()
output = [transform(line) for line in input_data]

# 한 번에 출력
print("\n".join(output))
