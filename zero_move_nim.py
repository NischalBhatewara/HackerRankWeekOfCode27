import functools

g = int(input().strip())
for game in range(g):
    n = int(input().strip())
    p = [int(p_temp) for p_temp in input().strip().split(' ')]
    p_xor = functools.reduce(lambda a, b: a ^ b, p)
    if p_xor == 0 and n % 2 == 0:
        print('L')
    else:
        print('W')
