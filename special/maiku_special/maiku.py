import math
[n, m] = [int(input()) for _ in range(2)]
answer = math.ceil(m/(n*2))
# 確認
print(answer)
