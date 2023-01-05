from collections import deque

visited = [False] * 9

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]]

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        n = queue.popleft()
        print(n, end = " ")

        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)