n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
for a0 in range(q):
    angle = int(input().strip())

hack_numbers = {1: 1, 2: 2, 3: 3}
rotation_diff = {0: 0}


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


def store_differences(matrix):
    size = len(matrix)
    temp_matrix = []
    for j in range(0, size):
        temp_row = []
        for i in range(size - 1, -1, -1):
            temp_row.append(matrix[i][j])
        temp_matrix.append(temp_row)
    print(temp_matrix)


store_differences(get_hackonacci_matrix(4))
