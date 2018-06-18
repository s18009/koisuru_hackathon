N = int(input())
alist = map(int,input().split()[:N])
nums = ((N + 1) // 2)
numver = nums - 1
alist = sorted(alist)
answer = alist[nums - 1]

print(answer)
