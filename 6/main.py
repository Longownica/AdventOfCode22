'''
[N]     [C]                 [Q]
[W]     [J] [L]             [J] [V]
[F]     [N] [D]     [L]     [S] [W]
[R] [S] [F] [G]     [R]     [V] [Z]
[Z] [G] [Q] [C]     [W] [C] [F] [G]
[S] [Q] [V] [P] [S] [F] [D] [R] [S]
[M] [P] [R] [Z] [P] [D] [N] [N] [M]
[D] [W] [W] [F] [T] [H] [Z] [W] [R]
 1   2   3   4   5   6   7   8   9

'''

if __name__ == '__main__':

    with open('crates.txt') as file:

        stack0 = []
        stack1 = ['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N']
        stack2 = ['W', 'P', 'Q', 'G', 'S']
        stack3 = ['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C']
        stack4 = ['F', 'Z', 'P', 'C', 'G', 'D', 'L']
        stack5 = ['T', 'P', 'S']
        stack6 = ['H', 'D', 'F', 'W', 'R', 'L']
        stack7 = ['Z', 'N', 'D', 'C']
        stack8 = ['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q']
        stack9 = ['R', 'M', 'S', 'G', 'Z', 'W', 'V']
        stacks = [stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

        while True:
            line = file.readline()
            if not line:
                break

            xtemp = line.split(" ")
            howMany = int(xtemp[1])
            fromWhere = int(xtemp[3])
            toWhere = int(xtemp[5])
            temp = []

            for i in range(howMany):
                #temp = stacks[fromWhere].pop()
                #stacks[toWhere].append(temp)
                temp.append(stacks[fromWhere].pop())

            for i in range(howMany):
            # temp = stacks[fromWhere].pop()
            # stacks[toWhere].append(temp)
                stacks[toWhere].append(temp.pop())

        for i in range(1, 10):
            if stacks[i]:
                print(stacks[i].pop())
            else:
                print("EMPTY")