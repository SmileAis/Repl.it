# NxM 얼음틀
# 뚫려있는 부분은 0, 막힌부부은 1, 0이 상하좌우가 연결되어있으면 붙어있는 것
# 생성되는 총 개수

n, m = map(int, input().split())
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


def dfs(x, y):
    if x<0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print(result)


