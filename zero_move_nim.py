import functools

g = int(input().strip())
for game in range(g):
    n = int(input().strip())
    p = [int(p_temp) for p_temp in input().strip().split(' ')]
    print(functools.reduce(lambda a, b: a ^ b, p))
