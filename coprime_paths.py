# algo: 1. do BFS and find shortest path
#       2. for each edge btw u, v:
#           if gcd(u, v) == 1:
#               coprime_edge += 1

n, q = input().strip().split(' ')
n, q = [int(n), int(q)]

nodes = [int(nodes_temp) for nodes_temp in input().strip().split(' ')]
edge_matrix = [[-1] * n for i in range(n)]

for edges_i in range(n - 1):
    edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
    # adding vales to edge matrix
    edge_matrix[edges_t[0] - 1][edges_t[1] - 1] = 1
    edge_matrix[edges_t[0] - 1][edges_t[0] - 1] = 0
    edge_matrix[edges_t[1] - 1][edges_t[1] - 1] = 0
    edge_matrix[edges_t[1] - 1][edges_t[0] - 1] = 1


def get_path(start, end):
    # init
    nodes_seen = [0] * n
    nodes_parent = [-1] * n
    queue = [start]
    nodes_seen[start] = 1
    flag = True

    if start == end:
        return [start + 1]

    # BSF algorithm
    while flag and len(queue) != 0:
        cur_node = queue.pop(0)
        for i in range(n):
            if edge_matrix[cur_node][i] == 1 and nodes_seen[i] != 1:
                nodes_seen[i] = 1
                queue.append(i)
                nodes_parent[i] = cur_node
        if cur_node == end:
            flag = False

    # don't need path, only need nodes in the path
    path = []
    i = end
    while i != -1:
        path.append(i + 1)
        i = nodes_parent[i]

    return path[::-1]


def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


for a0 in range(q):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]

    print("\nFor", u, v)
    path_nodes = get_path(u - 1, v - 1)
    print(path_nodes)
    coprime_count = 0
    for i in range(len(path_nodes)):
        for j in range(i + 1, len(path_nodes)):
            # get gcd
            if gcd(path_nodes[i], path_nodes[j]) == 1:
                coprime_count += 1

    print(coprime_count)
