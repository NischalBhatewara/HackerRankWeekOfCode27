# algo: 1. do BFS and find shortest path
#       2. for each edge btw u, v:
#           if gcd(u, v) == 1:
#               coprime_edge += 1
n, q = input().strip().split(' ')
n, q = [int(n), int(q)]

nodes_seen = [0] * n
nodes_parent = [-1] * n
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
    queue = [start]
    nodes_seen[start] = 1
    flag = True

    # BSF algorithm
    while flag:
        cur_node = queue.pop(0)
        print(cur_node)
        print([edge_matrix[cur_node - 1][i] for i in range(n)])

    return


for a0 in range(q):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    get_path(u, v)
