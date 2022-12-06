if __name__ == '__main__':

    with open('sections.txt') as file:

        result = 0
        while True:
            line = file.readline()
            if not line:
                break

            temp = line.split(',')
            temp1 = str(temp).split('-')
            temp2 = str(temp1).split(',')

            firstElfLeft = temp1[0]
            firstElfLeft = int(''.join(i for i in firstElfLeft if i.isdigit()))

            firstElfRight = temp2[1]
            firstElfRight = int(''.join(i for i in firstElfRight if i.isdigit()))

            secondElfLeft = temp2[2]
            secondElfLeft = int(''.join(i for i in secondElfLeft if i.isdigit()))

            secondElfRight = temp2[3]
            secondElfRight = int(''.join(i for i in secondElfRight if i.isdigit()))

            if firstElfLeft <= secondElfLeft <= firstElfRight:
                result = result + 1
            elif secondElfLeft <= firstElfLeft <= secondElfRight:
                result = result + 1

        print(result)