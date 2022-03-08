# The numbers 1 to 9999 (decimal base) were written on a paper.
# Then the paper was partially eaten by worms. It happened that just those parts of paper
# with digit "0" were eaten.
# Consequently the numbers 1200 and 3450 appear as 12 and 345 respectively,
# whilst the number 6078 appears as two separate numbers 6 and 78.
# What is the sum of the numbers appearing on the worm-eaten paper?

###### WHAT ARE WE LOOKING FOR
# to see your ability to :
# 1) write readable clean code
# 2) problem solving using (if/else/loops/etc ... )
# 3) use parsing, string/numbers dancing

# the "main" function is provided to get you started.

def worms(param):
    total=0
    inter=[]
    for i in param:
        inter=str(i).split('0')
        print(str(i))
        print(inter)
        for j in inter:
            if j:
                total+=int(j)
        
    return total


def main():
    print(worms(range(1, 101)))

if __name__ == '__main__':
    main()




