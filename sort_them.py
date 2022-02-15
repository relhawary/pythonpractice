import random

###### THE PROBLEM
# You have a list of numbers in an array (1 dimentional) , with the following characteristics :
# 1- it contains numbers from 5000 to 10000
# 2- numbers are not in order
# 3- no repeated numbers.
# 4- the array will be always the same number of elements.
# 5- there are no gaps in the numbers

# It is required to return a sorted array in the most optimized possible way.

###### WHAT ARE WE LOOKING FOR
# to see your ability to :
# 1) write readable clean code
# 2) problem solving using (if/else/loops/etc ... )
# 3) arrays and efficient code

# the "main" function is provided to get you started.

def sort_it(matrix):
    result = matrix
    return result

# Everything below is a helper code, you can ignore it.


def print_matrix(param):
    for row in param:
        print('{:5}'.format(row))

    return


def main():

    matrix = list(range(5000 , 10001))
    random.shuffle( matrix)

    matrix_str= ["" for x in range(5000)]
    for i in range(5000):
        matrix_str[i] = str(matrix[i] )

    print_matrix(sort_it(matrix_str))


if __name__ == '__main__':
    main()




