if __name__ == '__main__':

    points = 0
    myChoice = 'W'
    opponentChoice = 'D'

    with open('game.txt') as file:
        for line in file:
            opponentChoice = line[0]
            myChoice = line[2]

            #  first part
            '''
            if opponentChoice == 'A':
                if myChoice == 'X':  #rock vs rock
                    points = points + 1 + 3
                elif myChoice == 'Y':  #rock vs paper
                    points = points + 2 + 6
                elif myChoice == 'Z':  #rock vs scissors
                    points = points + 3 + 0

            elif opponentChoice == 'B':
                if myChoice == 'X':  #paper vs rock
                    points = points + 1 + 0
                elif myChoice == 'Y':  #paper vs paper
                    points = points + 2 + 3
                elif myChoice == 'Z':  #paper vs scissors
                    points = points + 3 + 6

            if opponentChoice == 'C':
                if myChoice == 'X':  #scissors vs rock
                    points = points + 1 + 6
                elif myChoice == 'Y':  #scissors vs paper
                    points = points + 2 + 0
                elif myChoice == 'Z':  #scissors vs scissors
                    points = points + 3 + 3
            '''

            #  second part
            if opponentChoice == 'A':
                if myChoice == 'X':  # rock, i lose
                    points = points + 3 + 0
                elif myChoice == 'Y':  # rock, i draw
                    points = points + 1 + 3
                elif myChoice == 'Z':  # rock, i win
                    points = points + 2 + 6

            elif opponentChoice == 'B':
                if myChoice == 'X':  # paper, i lose
                    points = points + 1 + 0
                elif myChoice == 'Y':  # paper, i draw
                    points = points + 2 + 3
                elif myChoice == 'Z':  # paper, i win
                    points = points + 3 + 6

            if opponentChoice == 'C':
                if myChoice == 'X':  # scissors, i lose
                    points = points + 2 + 0
                elif myChoice == 'Y':  # scissors, i draw
                    points = points + 3 + 3
                elif myChoice == 'Z':  # scissors, i win
                    points = points + 1 + 6

        print(points)