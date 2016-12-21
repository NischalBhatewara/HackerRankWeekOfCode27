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


# def store_differences(matrix):
#     temp_matrix = []
#     for i in range(1, 4):
#         for i in range()

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(0, 3):
    for j in range(0, 3):
        print(mat[i][j], end="\t")
    print()
print("\n")
for j in range(0, 3):
    for i in range(2, -1, -1):
        print(i, j, end="\t")
    print()
print()
for j in range(0, 3):
    for i in range(2, -1, -1):
        print(mat[i][j], end="\t")
    print()
