import random

# The method "find_7000(array1 , array2)" receives 2 arrays .
# These arrays contain SOME repeated/matching numbers.
# Complete the code in method "find_7000(array1 , array2)" to find the numbers repeated.
# the "main" function is provided to get you started.

###### WHAT ARE WE LOOKING FOR
# to see your ability to :
# 1) write readable clean code
# 2) problem solving using (if/else/loops/etc ... )
# 3) arrays and efficient code


def find_7000(array1 , array2):
    # i=0
    # result=[]
    # while i < len(array1):
    #     if array1[i] in array2:
    #         result.append(array1[i])
    #     i+=1
    result=[i for i in array1 if i in array2]
    
    
    return result


# Everything below is a helper code, you can ignore it.

def print_matrix(array1 ,array2 ):
    for row1 in array1 :
        print('{:5}'.format(row1))

    print( "\n\n\n\n ############################################# ")

    for row2 in array2 :
        print('{:5}'.format(row2))

    return


def main():

    array = list(range(5000 , 28001))
    random.shuffle(array)

    array1 = [i for i in range(15000)]
    array2 = [i for i in range(15000)]

    for x in range(15000):
        array1[x] = array[x]
        array2[x] = array[8000+x]

    final=find_7000(array1 , array2)
    print(final,len(final))


if __name__ == '__main__':
    main()







