# you have a 2 dimentional matrix square, like below
#     0     1     2
#     3     4     5
#     6     7     8

# It is required to fill the code in "turn_array(param) " method in order to rotate the matrix number of shifts clockwise.
# Here are some examples
# for 0 shifts
#     0     1     2
#     3     4     5
#     6     7     8

# for 1 shift
#     3     0     1
#     6     4     2
#     7     8     5

# for 2 shift2
#     6     3     0
#     7     4     1
#     8     5     2


# The matrix WILL BE square , i.e. height = width
# Matrix width > 2

###### WHAT ARE WE LOOKING FOR
# to see your ability to :
# 1) write readable clean code
# 2) problem solving using (if/else/loops/etc ... )
# 3) arrays and data structures

# the "main" function is provided to get you started.

# Please modify this method

#this works only for width=3 and doesnt work for others
def turn_array(param , shifts ):
    #print(param)
    x=len(param)
    newparam=[[0 for x in range(len(param))] for y in range(len(param))]
    #newrow=[]
    for rows in range(len(param)):
        for cols in range(len(param)):
            #print(rows,cols)
            if rows==0 and cols<=len(param)-1-shifts:
                newparam[rows][cols+shifts]=param[rows][cols]
            elif rows <= len(param)-1-shifts and cols > len(param)-1-shifts:
                newparam[rows+shifts][cols]=param[rows][cols]
            elif rows > len(param)-1-shifts and cols >= len(param)-1-shifts:
                newparam[rows][cols-shifts]=param[rows][cols]
            elif rows>=len(param)-1-shifts and cols == 0:
                newparam[rows-shifts][cols]=param[rows][cols]
            else:
                newparam[rows][cols]=param[rows][cols] 
    return newparam

# Everything below is a helper code, you can ignore it.
#
#


def print_matrix(param):
    for row in param:
        for val in row:
            print('{:5}'.format(val), end='')
        print()

    return


def main():
    width = 3
    matrix = [[(x + width*y)for x in range(width)] for y in range(width)]

    print_matrix(matrix)
    print("\n")
    print_matrix(turn_array(matrix, 1))


if __name__ == '__main__':
    main()









