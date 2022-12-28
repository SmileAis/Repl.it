# Greed Algorithm
# 거스름돈으로 500원, 100원, 50원, 10원을 사용한다.
# 거슬러줘야 할 돈이 N원 일 때, 거슬러 줘야 할 동전의 최소 개수?
# 단, 거스름 돈은 항상 10의 배수이다.

exchange = int(input('거스름돈 입력 >> '))

coin_types = [500, 100, 50, 10]
coin_count = {500:0, 100:0, 50:0, 10:0}
count = 0

for coin in coin_types:
    cur_count = exchange // coin
    coin_count[coin] = cur_count
    
    exchange = exchange % coin

print(coin_count)
print(sum(coin_count.values()))