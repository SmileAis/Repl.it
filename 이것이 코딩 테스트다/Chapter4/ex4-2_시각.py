# 정수 N입력
# 0시 0분 0초 ~ N시 59분 59초 시간 중 3이 들어간 횟수

# 3중 반복
n = int(input('n 입력 >> '))
count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if '3' in time:
                count += 1

print(count)