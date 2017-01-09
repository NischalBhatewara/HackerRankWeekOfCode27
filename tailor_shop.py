# HR accepted.

import math

n, p = input().strip().split(' ')
n, p = [int(n), int(p)]
a = [math.ceil(int(a_temp) / p) for a_temp in input().strip().split(' ')]

# button_array = []
# for cluster_size in clusters:
#     if cluster_size in button_array:
#         cluster_size = max(button_array) + 1
#     button_array.append(cluster_size)
#     tot_buttons += cluster_size
a.sort()
# print(a)
tot_buttons = 0
button_max = 0
for size in a:
    if size <= button_max:
        size = button_max + 1
    button_max, tot_buttons = size, tot_buttons + size

print(tot_buttons)
