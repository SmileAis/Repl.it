from collections import deque
from pprint import pprint

n, m = map(int, input().split())

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

x = 0
y = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
is_first = True
def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= m or graph[mx][my] == 0:
                continue

            if graph[mx][my] == 1:
                graph[mx][my] = graph[x][y] + 1
                if is_first:
                    graph[0][0] = -1
                queue.append((mx, my))
    pprint(graph)
    return graph[n-1][m-1]

print(bfs(0, 0))