n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
for a0 in range(q):
    angle = int(input().strip())

hack_numbers = {1: 1, 2: 2, 3: 3}


def hackonacci(n):
    if n in hack_numbers:
        return hack_numbers[n]
    else:
        hn = hackonacci(n - 1) + 2 * hackonacci(n - 2) + 3 * hackonacci(n - 3)
        hack_numbers[n] = hn
        return hn


def get_hackonacci_matrix(size):
    matrix = []
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            hn = hackonacci((i * j) ** 2)
            row.append('X' if hn % 2 == 0 else 'Y')
        matrix.append(row)
    return matrix


print(get_hackonacci_matrix(n))
