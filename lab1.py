# BÀI 1

def snippet_1(n):
    total = 0

    for i in range(n):
        total = total + 1

    return total


# Độ phức tạp: O(n)


def snippet_2(n):
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    return count


# Độ phức tạp: O(n^2)


def snippet_3(n):
    steps = 0

    while n > 0:
        n = n // 2
        steps += 1

    return steps


# Độ phức tạp: O(log n)


def constant_work():
    x = 1
    y = 2
    z = x + y

    return z


def snippet_4(n):
    for i in range(n):
        constant_work()


# Độ phức tạp: O(n)


# BÀI 2


def snippet_5(n):
    total = 0

    for i in range(n):
        for j in range(i):
            total += 1

    return total


# Độ phức tạp: O(n^2)


def snippet_6(n):
    k = 1
    total = 0

    while k < n:
        for i in range(n):
            total += 1

        k = k * 2

    return total


# Độ phức tạp: O(n log n)


def snippet_7(arr):
    count = 0

    for x in arr:
        if x in arr:
            count += 1

    return count


# Độ phức tạp: O(n^2)


def snippet_8(arr):
    s = set(arr)

    count = 0

    for x in arr:
        if x in s:
            count += 1

    return count


# Độ phức tạp: O(n)


# BÀI 3


def two_sum_quadratic(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):

            if arr[i] + arr[j] == target:
                return (i, j)

    return None


# Độ phức tạp: O(n^2)


def two_sum_linear(arr, target):
    seen = {}

    for i in range(len(arr)):

        complement = target - arr[i]

        if complement in seen:
            return (seen[complement], i)

        seen[arr[i]] = i

    return None


# Độ phức tạp: O(n)


import time
import random

arr = list(range(100000))
random.shuffle(arr)
target = arr[123] + arr[9876]
start = time.time()
print(two_sum_linear(arr, target))
print("O(n) time:", time.time() - start)