def solve():
    ans = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans  # 233168


print(solve())
