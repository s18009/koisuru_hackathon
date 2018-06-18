count = 0
for [d, e] in [input().split() for _ in range(5)]:
    if d == e:
        count += 1
answer = "OK" if count >= 3 else "NG"
print(answer)
