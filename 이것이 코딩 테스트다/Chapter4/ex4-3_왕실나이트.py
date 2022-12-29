# 8x8 체스판, 행은 1~8, 열은 a~h
# 나이트가 움직일 수 있는 경우의 수?

point = input()

x = ord(point[0]) - ord('a') + 1
y = int(point[1])

moves = [[2, 1], [2, -1], [-2, 1], [-2, -1],
         [-1, 2], [1, 2], [1, -2], [-1, -2]]

count = 0
for move in moves:
    mx = x + move[0]
    my = y + move[1]
    print(mx, my)

    if mx < 1 or my < 1 or mx > 8 or my > 8:
        continue
    count += 1

print(count)