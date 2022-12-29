# A x N 크기의 정사각형 공간
# 가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (N, N)
# L, R, U, D중 하나의 문자가 반복
# 시작은 (1, 1), 최종 도착지?

x, y = 1, 1

size = int(input('사각형 크기 >> '))
moves = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_type = ['L', 'R', 'U', 'D']

for move in moves:
    idx = move_type.index(move)

    mx = x + dx[idx]
    my = y + dy[idx]

    if mx < 1 or my < 1 or mx > size or my > size:
        continue

    x = mx
    y = my

print('(', y, ',', x, ')')
        