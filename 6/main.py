import re

if __name__ == '__main__':

    with open('buffer.txt') as file:
        line = file.readlines()
        line = re.sub(r'[^a-zA-Z]', '', str(line))

        for el in range(4, len(line)):
            checkSet = {line[el - 4], line[el - 3], line[el - 2], line[el - 1]}
            if len(checkSet) == 4:
                print(el)
            break
