# 32217 광선 다각형 만들기
# 브론즈 1

import sys
input = sys.stdin.readline

def main():
    n = int(input().strip())
    thetas = list(map(int, input().split()))
    
    # i=1..n 에서의 입사각 θ_i 이므로,
    # 각 반사점 Ai의 내각 α_i = 2 * θ_i
    # (n+1)-각형 (A0,A1,...,An)의 내각 합은 ( (n+1) - 2 ) * 180 = (n - 1) * 180
    # 따라서 A0에서의 내각 α_0 = (n - 1) * 180 - sum_{i=1..n}(α_i)
    #                     = (n - 1) * 180 - sum_{i=1..n}(2 * θ_i)
    
    total_reflected = sum(thetas) * 2
    alpha_0 = (n - 1) * 180 - total_reflected
    
    print(alpha_0)

if __name__ == "__main__":
    main()