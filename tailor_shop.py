import math

n, p = input().strip().split(' ')
n, p = [int(n), int(p)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
clusters = [math.ceil(ai / p) for ai in a]
clusters.sort()

tot_buttons = 0
button_array = []
for cluster_size in clusters:
    if cluster_size in button_array:
        cluster_size = max(button_array) + 1
    button_array.append(cluster_size)

print(sum(button_array))
