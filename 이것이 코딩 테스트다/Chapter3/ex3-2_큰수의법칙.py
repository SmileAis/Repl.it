# 배열이 존재, 배열의 크기는 N
# M은 덧셈 횟수, K는 최대 덧셈 가능 횟수
# 가장 큰 결과를 가지는 합을 구하라.

n, m, k = map(int, input('배열크기, 덧셈 횟수, 최대 덧셈 횟수 >> ').split())
arr = list(map(int, input().split()))

arr.sort()
big1 = arr[-1]
big2 = arr[-2]

big2_num = m // (k + 1)
big1_num = m - big2_num

result = big1 * big1_num + big2 * big2_num

print(result)
