p = int(input())
numver = p // 100
nums = numver + 10
answer = numver if numver <= 10 else nums
# 確認用
print(answer)
