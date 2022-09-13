testcase = input()
ans = 0
for _ in testcase:
    num: int = int(input())
    key = 3
    while (num > 1):
        ans = ans + 1
        num = num-1
    print(ans)
