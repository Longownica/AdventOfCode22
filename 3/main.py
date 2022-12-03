from itertools import islice


def getvalue(letter):
    if ord(letter) > 97:  # lowercase
        return ord(letter) - 96
    else:
        return ord(letter) - 38


if __name__ == '__main__':

    with open('bags.txt') as file:

        result = 0
        elfId = 0
        for line in file:
            
            rucksackSize = int((len(line) - 1) / 2)

            for idx in range(rucksackSize + 1):
                if line[idx] in line[rucksackSize:]:
                    result = result + getvalue(line[idx])
                    break

    print("First answer ", result)


    with open('bags.txt') as file:

        result2 = 0
        while True:

            triples = list(islice(file, 3))
            if not triples:
                break

            shortestRucksack = min(triples, key=len)
            for item in shortestRucksack:
                if item in triples[0] and item in triples[1] and item in triples[2]:
                    result2 = result2 + getvalue(item)
                    break


        print("Secons answer ", result2)