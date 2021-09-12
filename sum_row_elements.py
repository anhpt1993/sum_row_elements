from get_matrix_number import input_row_col, get_number

def create_lst(number):
    array = []
    for i in range(number):
        array.append(get_number(0, 9))

    return tuple(array)

def create_tuple(row, col):
    return tuple([create_lst(col) for i in range(row)])

def sum_row_elements(row, col, *lst):
    array = []
    for j in range(col):
        sum = 0
        for i in range(row):
            sum += lst[i][j]
        array.append(sum)

    return tuple(array)

if __name__ == '__main__':
    row, col = input_row_col("Input two integer greater than 0 (separated by space): ")

    array = create_tuple(row, col)

    print("Initial Tuple: ")
    for i in array:
        print(i)

    new_tuple = sum_row_elements(row, col, *array)

    print(f"Sum row element: \n{new_tuple}")