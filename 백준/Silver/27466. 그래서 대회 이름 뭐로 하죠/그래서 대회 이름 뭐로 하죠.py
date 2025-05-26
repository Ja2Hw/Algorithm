import sys

def main() -> None:
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = input().strip()

    # 길이 자체가 불가능
    if M < 3 or M > N:
        print("NO")
        return

    vowels = set("AEIOU")

    # i 이후(자신 포함)에서 가장 왼쪽 자음 위치
    nxt_con = [-1] * (N + 1)
    for i in range(N - 1, -1, -1):
        nxt_con[i] = i if S[i] not in vowels else nxt_con[i + 1]

    prev_a = -1           # 직전에 본 A 위치
    idx1 = idx2 = idx3 = -1   # A, A, C 세 글자의 인덱스

    for i in range(N):
        if S[i] != 'A':
            continue

        if prev_a != -1:                       # A를 두 개 연속 확보
            c = nxt_con[i + 1]                 # 그 뒤 첫 자음
            # 첫 번째 A가 M-3번째 자리 이후에 있어야 앞에서 M-3글자 선택 가능
            if c != -1 and prev_a >= M - 3:
                idx1, idx2, idx3 = prev_a, i, c
                break
        prev_a = i

    if idx1 == -1:                             # 못 찾음
        print("NO")
        return

    # 앞부분 M-3글자 → 무조건 첫 A 앞에서 뽑으면 순서·연속성 모두 안전
    prefix = S[:M - 3]
    T = prefix + S[idx1] + S[idx2] + S[idx3]

    print("YES")
    print(T)

if __name__ == "__main__":
    main()