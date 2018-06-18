[s, t] = [int(input()) for _ in range(2)]
CurrentIndex = t - 1
CharList = ["-" for i in range(s)]

CharList[CurrentIndex] = "+"

answer = "".join(CharList)

print(answer)
