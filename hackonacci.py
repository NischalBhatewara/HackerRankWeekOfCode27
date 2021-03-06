hack_pattern = {1: 'Y', 2: 'X', 3: 'Y', 4: 'X', 5: 'X', 6: 'Y', 0: 'Y'}  # pattern in hackonacci numbers
rotation_diff = {0: 0}  # stores differences


# returns the hackonacci matrix for a given size
def get_hackonacci_matrix(size):
    matrix = []
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(hack_pattern[(i * j) ** 2 % 7])  # using the found pattern
        matrix.append(row)
    return matrix


# calculates differences in 90deg turns
def store_differences(matrix):
    size = len(matrix)
    rotate_matrix = matrix
    for count in range(3):
        # rotate
        temp_matrix = []
        for j in range(0, size):
            temp_row = []
            for i in range(size - 1, -1, -1):
                temp_row.append(rotate_matrix[i][j])
            temp_matrix.append(temp_row)
        rotate_matrix = temp_matrix
        # compare
        diff_counter = 0
        for i in range(size):
            for j in range(size):
                if rotate_matrix[i][j] != matrix[i][j]:
                    diff_counter += 1
        # rotate the rotated matrix 90deg to get new rotation matrix
        rotation_diff[count + 1] = diff_counter


n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
store_differences(get_hackonacci_matrix(n))
for counter in range(q):
    angle = int(input().strip())
    # the magic
    print(rotation_diff[((angle / 90) % 4)])
