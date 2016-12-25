# current score: 35.56 on 80

# algo: 1. do BFS and find shortest path
#       2. for each edge btw u, v:
#           if gcd(u, v) == 1:
#               coprime_edge += 1

n, q = input().strip().split(' ')
n, q = [int(n), int(q)]

nodes = [int(nodes_temp) for nodes_temp in input().strip().split(' ')]
edge_dict = {}
# edge_matrix = [[-1] * n for i in range(n)]  # think this is causing problem
coprime_paths = {}

for edges_i in range(n - 1):
    edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
    # adding vales to edge matrix
    # edge_matrix[edges_t[0] - 1][edges_t[1] - 1] = 1
    # edge_matrix[edges_t[1] - 1][edges_t[0] - 1] = 1
    # add to list
    u = edges_t[0] - 1
    v = edges_t[1] - 1
    for x, y in [[u, v], [v, u]]:
        if x in edge_dict:
            edge_dict[x].append(y)
        else:
            edge_dict[x] = [y]


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
        # for i in range(n):
        #     if edge_matrix[cur_node][i] == 1 and nodes_seen[i] != 1:
        #         nodes_seen[i] = 1
        #         queue.append(i)
        #         nodes_parent[i] = cur_node
        neighbours = edge_dict[cur_node]
        for neighbour in neighbours:
            if nodes_seen[neighbour] != 1:
                nodes_seen[neighbour] = 1
                queue.append(neighbour)
                nodes_parent[neighbour] = cur_node
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


# cache all answers and print later
# for u in range(len(nodes)):
#     for v in range(u + 1, len(nodes)):
#         node_u = nodes[u]
#         node_v = nodes[v]
#         path_nodes = get_path(node_u - 1, node_v - 1)
#         coprime_count = 0
#         for i in range(len(path_nodes)):
#             for j in range(i + 1, len(path_nodes)):
#                 # get gcd
#                 a = nodes[path_nodes[i] - 1]
#                 b = nodes[path_nodes[j] - 1]
#                 if gcd(a, b) == 1:
#                     coprime_count += 1
#
#         coprime_paths[str(node_u) + str(node_v)] = coprime_count

for a0 in range(q):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]

    if u == v:
        print("0")
        continue

    if (str(v) + str(u)) in coprime_paths:
        print(coprime_paths[str(v) + str(u)])
        continue
    if (str(u) + str(v)) in coprime_paths:
        print(coprime_paths[str(u) + str(v)])
        continue

    path_nodes = get_path(u - 1, v - 1)
    coprime_count = 0
    for i in range(len(path_nodes)):
        for j in range(i + 1, len(path_nodes)):
            # get gcd
            a = nodes[path_nodes[i] - 1]
            b = nodes[path_nodes[j] - 1]
            if gcd(a, b) == 1:
                coprime_count += 1
    coprime_paths[str(u) + str(v)] = coprime_count

    print(coprime_count)
