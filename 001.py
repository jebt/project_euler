def solve(until):
    ans = 0
    for i in range(until + 1):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans  # 233168 for <1000, 233333333166666668 for <1_000_000_000


def sum_divisible_by(n, until):
    p = until // n
    return n * (p * (p + 1)) // 2


def solve_better(until):
    return sum_divisible_by(3, until) + sum_divisible_by(5, until) - sum_divisible_by(15, until)


target = 1000 - 1
# target = 1_000_000_000 - 1
# print(solve(target))
print(solve_better(target))
