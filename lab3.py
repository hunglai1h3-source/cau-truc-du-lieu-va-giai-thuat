# Bài 1: 

def permutations(nums):
    res = []

    def backtrack(path, remain):
        if len(path) == len(nums):
            res.append(path.copy())
            return

        for i in range(len(remain)):
            backtrack(path + [remain[i]], remain[:i] + remain[i+1:])

    backtrack([], nums)
    return res


def combinations(nums, k):
    res = []

    def backtrack(start, path):
        if len(path) == k:
            res.append(path.copy())
            return

        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return res


def subsets(nums):
    res = []

    def backtrack(start, path):
        res.append(path.copy())

        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return res


def binary_strings(n):
    res = []

    def backtrack(path):
        if len(path) == n:
            res.append(path)
            return

        backtrack(path + "0")
        backtrack(path + "1")

    backtrack("")
    return res


print("Hoán vị:", permutations([1, 2, 3]))
print("Tổ hợp:", combinations([1, 2, 3, 4], 2))
print("Tập con:", subsets([1, 2, 3]))
print("Chuỗi nhị phân:", binary_strings(3))

# Bài 2:

import time


def safe(board, row, col):
    for r in range(row):
        if board[r] == col or abs(r - row) == abs(board[r] - col):
            return False
    return True


def print_board(board):
    for c in board:
        print(". " * c + "Q " + ". " * (len(board) - c - 1))
    print()


def n_queens_no_pruning(n):
    res = []
    calls = 0
    board = []

    def valid():
        for i in range(n):
            for j in range(i + 1, n):
                if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                    return False
        return True

    def backtrack(row):
        nonlocal calls
        calls += 1

        if row == n:
            if valid():
                res.append(board.copy())
            return

        for col in range(n):
            board.append(col)
            backtrack(row + 1)
            board.pop()

    backtrack(0)
    return res, calls


def n_queens_pruning(n):
    res = []
    calls = 0
    board = []

    def backtrack(row):
        nonlocal calls
        calls += 1

        if row == n:
            res.append(board.copy())
            return

        for col in range(n):
            if safe(board, row, col):
                board.append(col)
                backtrack(row + 1)
                board.pop()

    backtrack(0)
    return res, calls


def compare(n):
    print("\nN-Queens N =", n)

    start = time.time()
    r1, c1 = n_queens_no_pruning(n)
    t1 = time.time() - start

    start = time.time()
    r2, c2 = n_queens_pruning(n)
    t2 = time.time() - start

    print("Không pruning:", len(r1), "lời giải,", c1, "lần gọi,", t1)
    print("Có pruning:", len(r2), "lời giải,", c2, "lần gọi,", t2)

    if r2:
        print("Một lời giải mẫu:")
        print_board(r2[0])


compare(4)
compare(5)

# Bài 3:

import time


def subset_sum_basic(nums, target):
    res = []
    calls = 0

    def backtrack(start, path, total):
        nonlocal calls
        calls += 1

        if total == target:
            res.append(path.copy())

        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]], total + nums[i])

    backtrack(0, [], 0)
    return res, calls


def subset_sum_pruning(nums, target):
    nums.sort()
    res = []
    calls = 0
    cut = 0

    def backtrack(start, path, total):
        nonlocal calls, cut
        calls += 1

        if total == target:
            res.append(path.copy())
            return

        if total > target:
            cut += 1
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                cut += 1
                continue

            if total + nums[i] > target:
                cut += 1
                break

            if total + sum(nums[i:]) < target:
                cut += 1
                break

            backtrack(i + 1, path + [nums[i]], total + nums[i])

    backtrack(0, [], 0)
    return res, calls, cut


def compare(nums, target):
    print("\nSubset Sum, target =", target)

    start = time.time()
    r1, c1 = subset_sum_basic(nums, target)
    t1 = time.time() - start

    start = time.time()
    r2, c2, cut = subset_sum_pruning(nums, target)
    t2 = time.time() - start

    print("Không pruning:", len(r1), "kết quả,", c1, "lần gọi,", t1)
    print("Có pruning:", len(r2), "kết quả,", c2, "lần gọi,", cut, "nhánh cắt,", t2)
    print("Kết quả mẫu:", r2[:5])


compare([1, 2, 3, 4, 5], 6)
compare(list(range(1, 20)), 50)