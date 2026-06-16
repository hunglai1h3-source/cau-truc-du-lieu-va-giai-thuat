import heapq

def dijkstra(graph, source):
    """
    Dijkstra: tìm đường đi ngắn nhất từ source đến tất cả các đỉnh.
    graph: dict {vertex: [(neighbor, weight), ...]}
    source: đỉnh bắt đầu
    """
    distances = {v: float('inf') for v in graph}
    distances[source] = 0

    parent = {v: None for v in graph}

    pq = [(0, source)]

    visited = set()

    while pq:
        current_dist, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        if current_dist > distances[u]:
            continue

        for v, w in graph[u]:
            new_dist = distances[u] + w

            if new_dist < distances[v]:
                distances[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))

    return distances, parent


def reconstruct_path(parent, source, target):
    """
    Dựng lại đường đi từ source đến target dùng mảng parent.
    """
    path = []
    cur = target

    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    if not path or path[0] != source:
        return None

    return path


def print_distances(distances, source):
    print(f"Bảng khoảng cách từ {source}:")

    for v in sorted(distances.keys()):
        d = distances[v]

        if d == float('inf'):
            print(f"  {source} -> {v}: INF (không tới được)")
        else:
            print(f"  {source} -> {v}: {d}")


def test_dijkstra():
    graph = {
        'A': [('B', 4), ('D', 1)],
        'B': [('A', 4), ('C', 2), ('E', 3)],
        'C': [('B', 2), ('F', 5)],
        'D': [('A', 1), ('E', 2)],
        'E': [('D', 2), ('B', 3), ('F', 1)],
        'F': [('E', 1), ('C', 5)]
    }

    source = 'A'
    distances, parent = dijkstra(graph, source)

    print_distances(distances, source)

    print("\nMảng parent:")
    for v in sorted(parent.keys()):
        print(f"  parent[{v}] = {parent[v]}")

    print("\nĐường đi chi tiết:")
    for v in sorted(graph.keys()):
        if v == source:
            continue

        path = reconstruct_path(parent, source, v)

        if path is None:
            print(f"  {source} -> {v}: không có đường đi")
        else:
            cost = distances[v]
            print(f"  {source} -> {v}: {' -> '.join(path)} (cost = {cost})")


if __name__ == "__main__":
    test_dijkstra()
def make_set(vertices):
    """
    Khởi tạo DSU: mỗi đỉnh là một nhóm riêng, parent[v] = v.
    """
    parent = {}

    for v in vertices:
        parent[v] = v

    return parent


def find(parent, v):
    """
    Tìm root của v, leo lên tới khi parent[v] == v.
    """
    while parent[v] != v:
        v = parent[v]

    return v


def union(parent, a, b):
    """
    Gộp nhóm chứa a và nhóm chứa b.
    """
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a


def demo_dsu_basic():
    vertices = ['A', 'B', 'C', 'D', 'E']
    parent = make_set(vertices)

    ops = [
        ("union", 'A', 'B'),
        ("union", 'C', 'D'),
        ("find", 'B'),
        ("union", 'B', 'C'),
        ("find", 'D'),
        ("find", 'E'),
    ]

    print("=== DSU BASIC ===")
    print("Parent ban đầu:", parent)

    for op in ops:
        if op[0] == "union":
            _, x, y = op
            print(f"\nThực hiện union({x}, {y})")
            union(parent, x, y)
        else:
            _, x = op
            root = find(parent, x)
            print(f"\nfind({x}) = {root}")

        print("Parent hiện tại:", parent)


def make_set_optimized(vertices):
    """
    Khởi tạo DSU với size để union by size.
    """
    parent = {}
    size = {}

    for v in vertices:
        parent[v] = v
        size[v] = 1

    return parent, size


def find_optimized(parent, v):
    """
    Path compression: nén đường đi về root.
    """
    if parent[v] != v:
        parent[v] = find_optimized(parent, parent[v])

    return parent[v]


def union_optimized(parent, size, a, b):
    """
    Union by size: gắn cây nhỏ vào cây lớn.
    """
    root_a = find_optimized(parent, a)
    root_b = find_optimized(parent, b)

    if root_a == root_b:
        return

    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]


def demo_dsu_optimized():
    vertices = ['A', 'B', 'C', 'D', 'E']
    parent, size = make_set_optimized(vertices)

    print("\n=== DSU OPTIMIZED ===")
    print("Parent ban đầu:", parent)
    print("Size ban đầu:", size)

    union_optimized(parent, size, 'A', 'B')
    print("\nSau union_optimized(A, B):")
    print("Parent:", parent)
    print("Size:", size)

    union_optimized(parent, size, 'C', 'D')
    print("\nSau union_optimized(C, D):")
    print("Parent:", parent)
    print("Size:", size)

    union_optimized(parent, size, 'B', 'C')
    print("\nSau union_optimized(B, C):")
    print("Parent:", parent)
    print("Size:", size)

    print("\nfind_optimized(D) =", find_optimized(parent, 'D'))
    print("Parent sau path compression:", parent)


def find_count_basic(parent, v):
    steps = 0

    while parent[v] != v:
        v = parent[v]
        steps += 1

    return v, steps


def find_count_optimized(parent, v):
    steps = 0

    def find_rec(x):
        nonlocal steps

        if parent[x] != x:
            steps += 1
            parent[x] = find_rec(parent[x])

        return parent[x]

    root = find_rec(v)
    return root, steps


def compare_basic_vs_optimized():
    print("\n=== SO SÁNH BASIC VS OPTIMIZED ===")

    n = 10
    vertices = list(range(n))

    parent_basic = make_set(vertices)

    for i in range(n - 1):
        parent_basic[i + 1] = i

    print("Parent basic dạng chuỗi dài:", parent_basic)

    root, steps = find_count_basic(parent_basic, n - 1)
    print(f"Basic find({n - 1}) = {root}, số bước = {steps}")

    parent_opt = make_set(vertices)

    for i in range(n - 1):
        parent_opt[i + 1] = i

    print("Parent optimized trước find:", parent_opt)

    root, steps = find_count_optimized(parent_opt, n - 1)
    print(f"Optimized find({n - 1}) = {root}, số bước = {steps}")
    print("Parent optimized sau path compression:", parent_opt)

    root, steps = find_count_optimized(parent_opt, n - 1)
    print(f"Gọi lại optimized find({n - 1}) = {root}, số bước = {steps}")


if __name__ == "__main__":
    demo_dsu_basic()
    demo_dsu_optimized()
    compare_basic_vs_optimized()

def kruskal_mst_basic(vertices, edges):
    """
    Kruskal MST dùng DSU basic.
    """
    edges_sorted = sorted(edges, key=lambda e: e[0])

    parent = make_set(vertices)

    mst = []
    total_weight = 0

    print("Cạnh sau khi sort (w, u, v):")
    for e in edges_sorted:
        print(" ", e)

    print("\nDuyệt từng cạnh:")

    for w, u, v in edges_sorted:
        root_u = find(parent, u)
        root_v = find(parent, v)

        print(f"Xét cạnh {u}-{v} (w={w}), root_u={root_u}, root_v={root_v}")

        if root_u != root_v:
            print("  -> Khác nhóm -> CHỌN cạnh này")
            mst.append((u, v, w))
            total_weight += w
            union(parent, u, v)
        else:
            print("  -> Cùng nhóm -> BỎ, tránh chu trình")

        if len(mst) == len(vertices) - 1:
            break

    return mst, total_weight


def kruskal_mst_optimized(vertices, edges):
    """
    Kruskal MST với DSU tối ưu: path compression + union by size.
    """
    edges_sorted = sorted(edges, key=lambda e: e[0])

    parent, size = make_set_optimized(vertices)

    mst = []
    total_weight = 0

    for w, u, v in edges_sorted:
        if find_optimized(parent, u) != find_optimized(parent, v):
            mst.append((u, v, w))
            total_weight += w
            union_optimized(parent, size, u, v)

        if len(mst) == len(vertices) - 1:
            break

    return mst, total_weight


def test_kruskal():
    vertices = ['A', 'B', 'C', 'D', 'E']

    edges = [
        (1, 'A', 'B'),
        (4, 'A', 'C'),
        (3, 'B', 'C'),
        (2, 'B', 'D'),
        (5, 'C', 'E'),
        (2, 'D', 'E'),
    ]

    print("=== KRUSKAL VỚI DSU BASIC ===")

    mst1, total1 = kruskal_mst_basic(vertices, edges)

    print("\nMST basic:")
    for u, v, w in mst1:
        print(f"  {u}-{v} (w={w})")

    print("Tổng trọng số:", total1)

    print("\n=== KRUSKAL VỚI DSU OPTIMIZED ===")

    mst2, total2 = kruskal_mst_optimized(vertices, edges)

    print("\nMST optimized:")
    for u, v, w in mst2:
        print(f"  {u}-{v} (w={w})")

    print("Tổng trọng số:", total2)

    print("\nSo sánh:")
    print("MST basic:", mst1)
    print("MST optimized:", mst2)
    print("Hai tổng trọng số bằng nhau:", total1 == total2)


if __name__ == "__main__":
    test_kruskal()