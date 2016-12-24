# algo: 1. do BFS and find shortest path
#       2. for each edge btw u, v:
#           if gcd(u, v) == 1:
#               coprime_edge += 1


def get_path(start, end):
    return


n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
nodes = [int(nodes_temp) for nodes_temp in input().strip().split(' ')]
edges = [[-1] * n for i in range(n)]
print(edges)
for edges_i in range(n - 1):
    edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
    # adding vales to edge matrix
    edges[edges_t[0] - 1][edges_t[1] - 1] = 1
    edges[edges_t[0] - 1][edges_t[0] - 1] = 0
    edges[edges_t[1] - 1][edges_t[1] - 1] = 0
    edges[edges_t[1] - 1][edges_t[0] - 1] = 1

for a0 in range(q):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]

print(edges)
