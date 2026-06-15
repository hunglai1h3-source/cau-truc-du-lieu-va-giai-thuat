from collections import deque

def build_graph(edges, directed=False):
    """
    Xây dựng đồ thị từ danh sách cạnh.
    directed = False: đồ thị vô hướng
    directed = True: đồ thị có hướng
    """
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)

        if not directed:
            graph[v].append(u)

    return graph


def bfs(graph, start):
    """
    BFS duyệt đồ thị theo chiều rộng.
    Dùng queue để duyệt lần lượt từng lớp.
    """
    if start not in graph:
        return []

    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def dfs_recursive(graph, start, visited=None, result=None):
    """
    DFS duyệt đồ thị theo chiều sâu bằng đệ quy.
    Đi sâu vào một nhánh trước rồi quay lui.
    """
    if start not in graph:
        return []

    if visited is None:
        visited = set()

    if result is None:
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

    return result


def count_connected_components(graph):
    """
    Đếm số thành phần liên thông trong đồ thị.
    Mỗi lần BFS từ một đỉnh chưa thăm là một component mới.
    """
    visited = set()
    components = []

    def bfs_component(start):
        queue = deque([start])
        visited.add(start)
        component = []

        while queue:
            vertex = queue.popleft()
            component.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return component

    for vertex in graph:
        if vertex not in visited:
            component = bfs_component(vertex)
            components.append(component)

    return len(components), components


print("===== BÀI 1: GRAPH TRAVERSAL =====")

print("\n--- Test build_graph ---")

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E")
]

graph_undirected = build_graph(edges, directed=False)
print("Đồ thị vô hướng:")
for vertex in graph_undirected:
    print(vertex, ":", graph_undirected[vertex])

graph_directed = build_graph(edges, directed=True)
print("\nĐồ thị có hướng:")
for vertex in graph_directed:
    print(vertex, ":", graph_directed[vertex])


print("\n--- Test BFS ---")

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

print("BFS từ A:", bfs(graph, "A"))
print("BFS từ D:", bfs(graph, "D"))


print("\n--- Test DFS Recursive ---")

print("DFS từ A:", dfs_recursive(graph, "A"))
print("DFS từ C:", dfs_recursive(graph, "C"))


print("\n--- Test Connected Components ---")

graph1 = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

count1, comps1 = count_connected_components(graph1)
print("Test 1 - Số components:", count1)
print("Components:", comps1)

graph2 = {
    "A": ["B"],
    "B": ["A"],
    "C": ["D", "E"],
    "D": ["C"],
    "E": ["C"],
    "F": []
}

count2, comps2 = count_connected_components(graph2)
print("Test 2 - Số components:", count2)
print("Components:", comps2)
def has_cycle_undirected(graph):
    """
    Phát hiện chu trình trong đồ thị vô hướng.
    Dùng DFS và biến parent để tránh nhầm cạnh quay về cha là chu trình.
    """
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True

        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True

    return False


def has_cycle_directed(graph):
    """
    Phát hiện chu trình trong đồ thị có hướng.
    WHITE: chưa thăm
    GRAY: đang xử lý
    BLACK: đã xử lý xong
    Nếu gặp lại đỉnh GRAY thì có chu trình.
    """
    WHITE = 0
    GRAY = 1
    BLACK = 2

    color = {}

    for vertex in graph:
        color[vertex] = WHITE
        for neighbor in graph[vertex]:
            if neighbor not in color:
                color[neighbor] = WHITE

    def dfs(vertex):
        color[vertex] = GRAY

        for neighbor in graph.get(vertex, []):
            if color[neighbor] == GRAY:
                return True

            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True

        color[vertex] = BLACK
        return False

    for vertex in color:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True

    return False


print("===== BÀI 2: CYCLE DETECTION =====")

print("\n--- Phần A: Đồ thị vô hướng ---")

graph1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print("Test 1 có chu trình:", has_cycle_undirected(graph1))

graph2 = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

print("Test 2 không có chu trình:", has_cycle_undirected(graph2))

graph3 = {
    0: [1],
    1: [0],
    2: [3, 4],
    3: [2, 4],
    4: [2, 3]
}

print("Test 3 đồ thị không liên thông có chu trình:", has_cycle_undirected(graph3))


print("\n--- Phần B: Đồ thị có hướng ---")

graph4 = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

print("Test 1 có chu trình A -> B -> C -> A:", has_cycle_directed(graph4))

graph5 = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print("Test 2 DAG không có chu trình:", has_cycle_directed(graph5))

graph6 = {
    "A": ["B"],
    "B": ["C"],
    "C": [],
    "D": ["C"]
}

print("Test 3 cross edge không có chu trình:", has_cycle_directed(graph6))


print("\nGiải thích:")
print("Đồ thị vô hướng dùng parent để tránh nhầm cạnh quay về cha.")
print("Đồ thị có hướng dùng WHITE, GRAY, BLACK để biết đỉnh đang xử lý hay đã xử lý xong.")
from collections import deque

def has_cycle_directed(graph):
    """
    Kiểm tra chu trình trong đồ thị có hướng bằng 3 màu.
    Dùng để hỗ trợ Topological Sort và Course Schedule.
    """
    WHITE = 0
    GRAY = 1
    BLACK = 2

    color = {}

    for vertex in graph:
        color[vertex] = WHITE
        for neighbor in graph[vertex]:
            if neighbor not in color:
                color[neighbor] = WHITE

    def dfs(vertex):
        color[vertex] = GRAY

        for neighbor in graph.get(vertex, []):
            if color[neighbor] == GRAY:
                return True

            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True

        color[vertex] = BLACK
        return False

    for vertex in color:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True

    return False


def topological_sort_dfs(graph):
    """
    Topological Sort bằng DFS.
    Chỉ dùng được nếu đồ thị không có chu trình.
    """
    if has_cycle_directed(graph):
        return None

    visited = set()
    stack = []

    def dfs(vertex):
        visited.add(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(vertex)

    all_vertices = list(graph.keys())

    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor not in all_vertices:
                all_vertices.append(neighbor)

    for vertex in all_vertices:
        if vertex not in visited:
            dfs(vertex)

    stack.reverse()
    return stack


def topological_sort_kahn(graph):
    """
    Topological Sort bằng Kahn's Algorithm.
    Tính in-degree, đỉnh nào in-degree = 0 thì đưa vào queue.
    """
    all_vertices = list(graph.keys())

    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor not in all_vertices:
                all_vertices.append(neighbor)

    in_degree = {}

    for vertex in all_vertices:
        in_degree[vertex] = 0

    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1

    queue = deque()

    for vertex in in_degree:
        if in_degree[vertex] == 0:
            queue.append(vertex)

    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(all_vertices):
        return None

    return result


def build_course_graph(num_courses, prerequisites):
    """
    Xây dựng đồ thị môn học.
    [a, b] nghĩa là muốn học a thì phải học b trước.
    Vì vậy tạo cạnh b -> a.
    """
    graph = {}

    for i in range(num_courses):
        graph[i] = []

    for a, b in prerequisites:
        graph[b].append(a)

    return graph


def can_finish(num_courses, prerequisites):
    """
    Course Schedule I.
    Trả về True nếu có thể học hết tất cả môn.
    Trả về False nếu có chu trình.
    """
    graph = build_course_graph(num_courses, prerequisites)

    if has_cycle_directed(graph):
        return False

    return True


def find_order(num_courses, prerequisites):
    """
    Course Schedule II.
    Trả về thứ tự học hợp lệ.
    Nếu không thể học hết thì trả về [].
    """
    graph = build_course_graph(num_courses, prerequisites)
    order = topological_sort_kahn(graph)

    if order is None:
        return []

    return order


print("===== BÀI 3: TOPOLOGICAL SORT VÀ COURSE SCHEDULE =====")

print("\n--- Test Topological Sort DFS ---")

graph1 = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

print("Topo DFS:", topological_sort_dfs(graph1))

graph2 = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

print("Topo DFS với đồ thị có chu trình:", topological_sort_dfs(graph2))


print("\n--- Test Topological Sort Kahn ---")

print("Topo Kahn:", topological_sort_kahn(graph1))
print("Topo Kahn với đồ thị có chu trình:", topological_sort_kahn(graph2))


print("\n--- Test Course Schedule ---")

n1 = 4
prerequisites1 = [
    [1, 0],
    [2, 0],
    [3, 1],
    [3, 2]
]

print("Test 1 có thể học hết:", can_finish(n1, prerequisites1))
print("Thứ tự học:", find_order(n1, prerequisites1))

n2 = 2
prerequisites2 = [
    [1, 0],
    [0, 1]
]

print("Test 2 không thể học hết:", can_finish(n2, prerequisites2))
print("Thứ tự học:", find_order(n2, prerequisites2))

n3 = 5
prerequisites3 = [
    [1, 0],
    [2, 0],
    [3, 1],
    [4, 3]
]

print("Test 3 có thể học hết:", can_finish(n3, prerequisites3))
print("Thứ tự học:", find_order(n3, prerequisites3))