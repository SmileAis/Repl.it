# N x M 크기의 직사각형
# 현재 위치 현재 방향에서 왼쪽 방향부터 이동
# 왼쪽에 가지 않은 칸이 있다면 왼쪽방향  회전후 전진, 없다면 왼쪽방향 회전
# 네 방향 이미 가본칸 or 바다인경우 바라보는 방향 유지하고 뒤로 한칸.
# 뒤가 바다칸인경우 움직임 멈춤

from pprint import pprint

m, n = map(int, input().split(" "))
x, y, dir = map(int, input().split(" "))

map_list = list()
for i in range(n):
    row = list(map(int, input().split(" ")))
    map_list.append(row)
pprint(map_list)

# 상 좌 우 하
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

count = 1
chk_all = 0
while(True):
    print(x, y)
    dir = (dir + 1) % 4
    mx = x + dx[dir]
    my = y + dy[dir]

    if mx < 0 or mx >= n or my < 0 or my >= m or map_list[mx][my]==1:
        chk_all += 1
        if chk_all == 4:
            mx = x - dx[dir]
            my = y - dy[dir]
            if mx < 0 or mx >= n or my < 0 or my >= m or map_list[mx][my] == 1:    
                break
            x = mx
            y = my
            chk_all = 0
        continue

    
    x = mx
    y = my
    map_list[x][y] = 2
    chk_all=0
    count += 1

print(count)
    
    
