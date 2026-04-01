def read_matrix():
    """Зчитує матрицю"""
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(float, input().split())))
    return matrix, n, m


def add_matrices(A, B, n, m):
    """Додає матриці"""
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


def multiply_by_constant(matrix, n, m, k):
    """Множить матрицю на число"""
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(matrix[i][j] * k)
        result.append(row)
    return result


def multiply_matrices(A, B, n1, m1, n2, m2):
    """Множить матриці"""
    result = []
    for i in range(n1):
        row = []
        for j in range(m2):
            s = 0
            for k in range(m1):
                s += A[i][k] * B[k][j]
            row.append(s)
        result.append(row)
    return result


def transpose_main(matrix, n, m):
    """Транспонування по головній діагоналі"""
    result = []
    for j in range(m):
        row = []
        for i in range(n):
            row.append(matrix[i][j])
        result.append(row)
    return result


def transpose_side(matrix, n, m):
    """Транспонування по побічній діагоналі"""
    result = []
    for j in range(m):
        row = []
        for i in range(n):
            row.append(matrix[n - 1 - i][m - 1 - j])
        result.append(row)
    return result


def transpose_vertical(matrix, n, m):
    """Відображення по вертикалі"""
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(matrix[i][m - 1 - j])
        result.append(row)
    return result


def transpose_horizontal(matrix, n, m):
    """Відображення по горизонталі"""
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(matrix[n - 1 - i][j])
        result.append(row)
    return result


def get_minor(matrix, row, col):
    """Повертає мінор"""
    minor = []
    for i in range(len(matrix)):
        if i != row:
            new_row = []
            for j in range(len(matrix)):
                if j != col:
                    new_row.append(matrix[i][j])
            minor.append(new_row)
    return minor


def determinant(matrix):
    """Обчислює визначник"""
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for j in range(n):
        det += ((-1) ** j) * matrix[0][j] * determinant(get_minor(matrix, 0, j))
    return det


def transpose_square(matrix):
    """Транспонує квадратну матрицю"""
    result = []
    for j in range(len(matrix)):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result


def inverse(matrix):
    """Знаходить обернену матрицю"""
    n = len(matrix)
    det = determinant(matrix)

    if det == 0:
        return None

    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            minor = get_minor(matrix, i, j)
            row.append(((-1) ** (i + j)) * determinant(minor))
        cofactors.append(row)

    cofactors = transpose_square(cofactors)

    for i in range(n):
        for j in range(n):
            cofactors[i][j] = cofactors[i][j] / det

    return cofactors


def print_matrix(matrix):
    """Виводить матрицю"""
    for row in matrix:
        print(*row)


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

    choice = input()

    if choice == "0":
        break

    elif choice == "1":
        A, n1, m1 = read_matrix()
        B, n2, m2 = read_matrix()

        if n1 != n2 or m1 != m2:
            print("ERROR")
        else:
            print_matrix(add_matrices(A, B, n1, m1))

    elif choice == "2":
        matrix, n, m = read_matrix()
        k = float(input())
        print_matrix(multiply_by_constant(matrix, n, m, k))

    elif choice == "3":
        A, n1, m1 = read_matrix()
        B, n2, m2 = read_matrix()

        if m1 != n2:
            print("The operation cannot be performed.")
        else:
            print_matrix(multiply_matrices(A, B, n1, m1, n2, m2))

    elif choice == "4":
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")

        t = input()
        matrix, n, m = read_matrix()

        if t == "1":
            print_matrix(transpose_main(matrix, n, m))
        elif t == "2":
            print_matrix(transpose_side(matrix, n, m))
        elif t == "3":
            print_matrix(transpose_vertical(matrix, n, m))
        elif t == "4":
            print_matrix(transpose_horizontal(matrix, n, m))

    elif choice == "5":
        matrix, n, m = read_matrix()
        print(determinant(matrix))

    elif choice == "6":
        matrix, n, m = read_matrix()
        result = inverse(matrix)

        if result is None:
            print("This matrix doesn't have an inverse.")
        else:
            print_matrix(result)