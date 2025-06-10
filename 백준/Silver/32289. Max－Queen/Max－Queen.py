import sys
input = sys.stdin.readline

def main():
    # 행의 개수 n, 열의 개수 m 입력
    n, m = map(int, input().split())

    # 1) 행 공격
    # 각 행마다 m개의 퀸이 있고, 인접한 퀸들만 서로 공격하므로
    # 한 행에서 (m - 1)개의 공격쌍, n개 행에 걸쳐 n * (m - 1)
    row_attacks = n * (m - 1)

    # 2) 열 공격
    # 각 열마다 n개의 퀸, 인접한 퀸들만 공격 → 한 열당 (n - 1), m개 열에 걸쳐 m * (n - 1)
    col_attacks = m * (n - 1)

    # 3) 대각선 공격 (NW-SE 방향)
    # 체스판 전체에 퀸이 n*m개, 이 방향의 대각선 수는 (n + m - 1)
    # 각 대각선에서 인접한 퀸들만 공격 → 총 공격쌍 = 전체 퀸 수 - 대각선 수
    diag1_attacks = n * m - (n + m - 1)

    # 4) 대각선 공격 (NE-SW 방향)
    # 계산 방법은 위와 동일
    diag2_attacks = n * m - (n + m - 1)

    # 네 방향에서의 공격쌍을 모두 합산
    answer = row_attacks + col_attacks + diag1_attacks + diag2_attacks

    # 결과 출력
    print(answer)

if __name__ == "__main__":
    main()
