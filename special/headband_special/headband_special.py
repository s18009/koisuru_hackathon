import math
[[n, p], [m, q]] = [map(int, input().split()) for _ in range(2)]
answer = math.ceil(n/m)*q + n * p
# 確認
print(answer)
