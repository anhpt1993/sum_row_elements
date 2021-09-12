import random
def input_row_col(text):
    while True:
        try:
            row, col = [int(x) for x in input(text).strip().split()]
            if row > 0 and col > 0:
                return row, col
                break
            else:
                print("\nInvalid Input. Try Again!!!\n".upper())
        except ValueError:
            print("\nInvalid Input. Try Again!!!\n".upper())

def get_number(min, max):
    return random.randint(min, max)

def create_array(row, col):
    array = []
    for i in range(row):
        array.append([get_number(0, 9) for j in range(col)])
    return array

if __name__ == '__main__':
    row, col = input_row_col("Input two integer greater than 0 (separated by space): ")
    array = create_array(row, col)
    for i in array:
        print(i)