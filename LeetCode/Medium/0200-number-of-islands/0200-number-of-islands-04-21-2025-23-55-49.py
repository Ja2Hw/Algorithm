# 섬의 수 : DFS(깊이 우선 탐색) 재귀
# 그래프 모양이 아니더라도 그래프형으로 변환해서 풀이할 수 있음
# 입력 값이 그래프는 아니지만 동서남북이 모두 연결된 그래프로 가정하고 동일한 형태로 처리할 수 있음
    # 네 뱡향 각각 DFS(깊이 우선 탐색) 재귀를 이용해 탐색을 끝마치면 1이 증가하는 형태로 육지의 개수를 파악할 수 있음

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 중첩 함수 -> 바깥에 위치한 함수와 달리 부모 함수의 변수를 읽을 수 있다는 장점이 있음
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            # 땅(1)이라면 물(0)로 변경 -> 방문 표시
            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # dfs()에서 빠져나왔다는 것은 근처에 있는 모든 1을 다 0으로 바꾸었다는 의미이므로
                    # 카운트 1 증가
                    count += 1
        
        return count