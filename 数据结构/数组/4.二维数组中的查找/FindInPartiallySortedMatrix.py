def find(matrix, rows, columns, number):
    if matrix is not None and rows > 0 and columns > 0:
        # 从右上角开始
        row = 0
        column = columns - 1
        while row < rows and column >= 0:
            if matrix[row][column] == number:
                return True
            elif matrix[row][column] > number:
                column -= 1
            else:
                row += 1
        return False
    return False


if __name__ == "__main__":
    case1 = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    case2 = []

    print('包含该数字', find(case1, 4, 4, 7))
    print('不含该数字', find(case1, 4, 4, 3))
    print('矩阵为空', find(case2, 0, 0, 7))
