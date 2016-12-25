# current score: 35.56 on 80

# algo: 1. do BFS and find shortest path
#       2. for each edge btw u, v:
#           if gcd(u, v) == 1:
#               coprime_edge += 1

n, q = input().strip().split(' ')
n, q = [int(n), int(q)]

nodes = [int(nodes_temp) for nodes_temp in input().strip().split(' ')]
edge_dict = {}
coprime_paths = {}

for edges_i in range(n - 1):
    edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
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
    queue_start = [start]
    queue_end = [end]
    nodes_seen[start] = 1
    flag = True
    common = -1
    connector = -1

    if start == end:
        return [start + 1]

    # BSF algorithm
    while flag and len(queue_start) != 0 and len(queue_end) != 0:
        cur_node_start = queue_start.pop(0)
        cur_node_end = queue_end.pop(0)
        neighbours_start = edge_dict[cur_node_start]
        neighbours_end = edge_dict[cur_node_end]
        for ne in neighbours_end:
            if ne in neighbours_start or ne == cur_node_start:
                common = ne
                nodes_parent[ne] = cur_node_start
                connector = cur_node_end
                flag = False
        if not flag:
            continue
        for neighbour in (neighbours_start + neighbours_end):
            if nodes_seen[neighbour] != 1:
                nodes_seen[neighbour] = 1
                if neighbour in neighbours_start:
                    queue_start.append(neighbour)
                    nodes_parent[neighbour] = cur_node_start
                else:
                    queue_end.append(neighbour)
                    nodes_parent[neighbour] = cur_node_end
        if cur_node_start == end:
            flag = False

    # don't need path, only need nodes in the path
    # path = []
    # i = end
    # while i != -1:
    #     path.append(i + 1)
    #     i = nodes_parent[i]

    path = []
    i = common
    while i != -1:
        path.append(i + 1)
        i = nodes_parent[i]
    i = connector
    while i != -1:
        path.append(i + 1)
        i = nodes_parent[i]

    return path


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
