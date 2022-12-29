# 어떤 수 N이 1이 될 때까지 다음 과정중 하나를 반복
# 1. N에서 1을 뺀다.
# 2. N에서 K로 나눈다.
# 최소 횟수를 구하라.

n, k = map(int, input('n, k입력 >> ').split())
count = 0

while(n > 1):
    if n // k != 0:
        count += n % k
        n -= n % k

    if n == 1:
        break
        
    n //= k
    count += 1
    
print(count)
                