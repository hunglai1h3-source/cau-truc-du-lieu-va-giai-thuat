# Bài 1:

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    res = []
    last = 0

    for start, end in activities:
        if start >= last:
            res.append((start, end))
            last = end

    return res


def coin_change_greedy(amount, coins):
    coins.sort(reverse=True)
    res = []

    for coin in coins:
        while amount >= coin:
            res.append(coin)
            amount -= coin

    if amount == 0:
        return len(res), res
    return -1, []


def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total = 0
    res = []

    for weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total += value
            capacity -= weight
            res.append((weight, value, 1))
        else:
            part = capacity / weight
            total += value * part
            res.append((weight, value, part))
            capacity = 0

    return total, res


def min_intervals_remove(intervals):
    keep = activity_selection(intervals)
    return len(intervals) - len(keep)


print("Activity Selection:")
print(activity_selection([(1, 4), (3, 5), (0, 6), (5, 7), (8, 11), (12, 16)]))
print(activity_selection([(1, 3), (2, 4), (3, 5), (4, 6)]))

print("\nCoin Change Greedy:")
print(coin_change_greedy(63, [25, 10, 5, 1]))
print(coin_change_greedy(30, [25, 10, 1]))

print("\nFractional Knapsack:")
print(fractional_knapsack(50, [(10, 60), (20, 100), (30, 120)]))
print(fractional_knapsack(60, [(10, 500), (20, 300), (30, 400)]))

print("\nMinimum Intervals Remove:")
print(min_intervals_remove([(1, 2), (2, 3), (3, 4), (1, 3)]))
print(min_intervals_remove([(1, 2), (1, 2), (1, 2)]))

# Bài 2:

import heapq
import time


def coin_change_greedy(amount, coins):
    coins.sort(reverse=True)
    res = []

    for coin in coins:
        while amount >= coin:
            res.append(coin)
            amount -= coin

    if amount == 0:
        return len(res), res
    return -1, []


def min_meeting_rooms(meetings):
    if not meetings:
        return 0

    meetings.sort()
    heap = []

    for start, end in meetings:
        if heap and start >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, end)

    return len(heap)


def coin_change_dp(amount, coins):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float("inf"):
        return -1
    return dp[amount]


def compare_coin_change(amount, coins):
    print("\nCoin Change:", amount, coins)

    start = time.time()
    g, detail = coin_change_greedy(amount, coins.copy())
    tg = time.time() - start

    start = time.time()
    d = coin_change_dp(amount, coins)
    td = time.time() - start

    print("Greedy:", g, detail, "time:", tg)
    print("DP:", d, "time:", td)

    if g == d:
        print("Greedy đúng")
    else:
        print("Greedy sai, DP tối ưu hơn")


print("Meeting Rooms:")
print(min_meeting_rooms([(0, 30), (5, 10), (15, 20)]))
print(min_meeting_rooms([(7, 10), (2, 4)]))
print(min_meeting_rooms([(1, 5), (2, 6), (6, 8)]))

compare_coin_change(67, [25, 10, 5, 1])
compare_coin_change(30, [25, 10, 1])

# Bài 3:

import time
import random


def find_content_children(greed, cookies):
    greed.sort()
    cookies.sort()

    i = 0
    j = 0

    while i < len(greed) and j < len(cookies):
        if cookies[j] >= greed[i]:
            i += 1
        j += 1

    return i


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def assign_bikes(workers, bikes):
    pairs = []

    for i in range(len(workers)):
        for j in range(len(bikes)):
            d = manhattan_distance(workers[i], bikes[j])
            pairs.append((d, i, j))

    pairs.sort()

    used_workers = set()
    used_bikes = set()
    result = []

    for d, i, j in pairs:
        if i not in used_workers and j not in used_bikes:
            used_workers.add(i)
            used_bikes.add(j)
            result.append((i, j, d))

        if len(used_workers) == len(workers):
            break

    return result


def generate_test_data(n):
    data = []

    for i in range(n):
        start = random.randint(0, 100)
        end = start + random.randint(1, 20)
        data.append((start, end))

    return data


def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    res = []
    last = 0

    for start, end in activities:
        if start >= last:
            res.append((start, end))
            last = end

    return res


def benchmark():
    for n in [100, 500, 1000]:
        data = generate_test_data(n)

        start = time.time()
        activity_selection(data)
        t = time.time() - start

        print("n =", n, "time =", t)


print("Assign Cookies:")
print(find_content_children([1, 2, 3], [1, 1]))
print(find_content_children([1, 2], [1, 2, 3]))

print("\nAssign Bikes:")
print(assign_bikes([(0, 0), (2, 1)], [(1, 2), (3, 3)]))

print("\nBenchmark:")
benchmark()