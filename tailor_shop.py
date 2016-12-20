import math

n, p = input().strip().split(' ')
n, p = [int(n), int(p)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
clusters = [math.ceil(ai / p) for ai in a]
# # clusters.sort()
#
# tot_buttons = 0
# button_array = []
# for cluster_size in clusters:
#     if cluster_size in button_array:
#         cluster_size = max(button_array) + 1
#     button_array.append(cluster_size)
#     tot_buttons += cluster_size

# print(tot_buttons)

unique = set(clusters)
not_unique = set(([x for x in clusters if clusters.count(x) > 1]))

print("not unique:", not_unique)
print("unique:", unique)

max_unique = max(unique)
tot_with_max = max_unique + len(not_unique)
start = max_unique + 1

sum_not_unique = (tot_with_max * (tot_with_max + 1)) - (start * (start + 1))
sum_not_unique *= 0.5

print(sum(unique) + sum_not_unique)
