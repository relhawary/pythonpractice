###### THE PROBLEM

# Write a program that prints the numbers from 1 to 100.
# But
# for multiples of three print "Alpha" instead of the number
# for multiples of five print "Beta" instead of the number
# for numbers which are multiples of both three and five print "AlphaBeta"

###### WHAT ARE WE LOOKING FOR
# to see your ability to :
# 1) write readable clean code
# 2) problem solving using (if/else/loops/etc ... )

# the "main" function is provided to get you started.

# you can use this method
def run_code(my_array):
    #result = my_array 
    result=[]
    for i in my_array:
        if i%5==0 and i%3==0:
            result.append("AlphaBeta")
        elif i%5==0:
            result.append("Beta")
        elif i%3==0:
            result.append("Alpha")
        else:
            result.append(i)
    return result


def main():
    print(run_code(range(1, 50)))


if __name__ == '__main__':
    main()





