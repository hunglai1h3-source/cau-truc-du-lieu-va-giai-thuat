# Bài 1:
def sum_to_n(n):
    if n == 0:
        return 0

    return n + sum_to_n(n - 1)


def power(n, k):
    if k == 0:
        return 1

    return n * power(n, k - 1)


def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


print(sum_to_n(5))
print(power(2, 5))
print(reverse_string("hello"))
print(is_palindrome("racecar"))

# Bài 2:

import time


def fibonacci_naive(n):
    if n <= 1:
        return n

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


def fibonacci_iterative(n):
    if n <= 1:
        return n

    a = 0
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


print(fibonacci_naive(10))
print(fibonacci_memo(100))
print(fibonacci_iterative(100))

start = time.time()
fibonacci_naive(30)
print("Naive:", time.time() - start)

start = time.time()
fibonacci_memo(100)
print("Memo:", time.time() - start)

# Bài 3: 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [64, 34, 25, 12, 22, 11, 90]

print("Mảng ban đầu:", arr)
print("Sau khi sắp xếp:", merge_sort(arr))