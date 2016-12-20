import math

n, p = input().strip().split(' ')
n, p = [int(n), int(p)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
# clusters.sort()

tot_buttons = 0
# button_array = []
# for cluster_size in clusters:
#     if cluster_size in button_array:
#         cluster_size = max(button_array) + 1
#     button_array.append(cluster_size)
#     tot_buttons += cluster_size
button_max = 0
for cluster_cost in a:
    size = math.ceil(cluster_cost / p)
    if size <= button_max:
        size = button_max + 1
    button_max, tot_buttons = size, tot_buttons + size

print(tot_buttons)
