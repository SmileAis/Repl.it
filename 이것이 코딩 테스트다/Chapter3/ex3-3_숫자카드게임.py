# 숫자 카드 N x M 형태
# 행을 먼저 선택하고, 그 행의 가장 낮은 카드를 뽑는다.
# 최종적으로 가장 높은 카드를 뽑도록 한다.

n, m = map(int, input('행, 열 입력 >> ').split())
data = []

for _ in range(n):
    row = list(map(int, input().split()))
    data.append(min(row))

result = max(data)

print(result)