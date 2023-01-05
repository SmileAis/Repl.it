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

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")

    for n in graph[start]:
        if not visited[n]:
            dfs(graph, n, visited)


dfs(graph, 3, visited)

    