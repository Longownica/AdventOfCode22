import functools

if __name__ == '__main__':
    with open('elves.txt') as f:
        lines = f.readlines()

    # read data and clean all new lines \n
    calories = list(lines)
    for idx, elem in enumerate(calories):
        calories[idx] = ''.join(i for i in calories[idx] if i.isdigit())

    # create list of lists for each elf
    elves = []
    id = 0
    tempList = []
    for idx, elem in enumerate(calories):
        if calories[idx] != '':
            tempList.append(calories[idx])
        else:
            elves.insert(id, tempList)
            tempList = []
            id = id + 1

    # string to int
    for i, elf in enumerate(elves):
        elves[i] = [int(x) for x in elves[i]]

    # sum calories for each elf
    for idx, elf in enumerate(elves):
        elves[idx] = (functools.reduce(lambda a, b: a + b, elf))

    # result
    result = max(elves)
    print("The elf who carry the most calories has:", result, "of it")

    # _______________________________________________________
    # here i got 1 star!

    topThree = (sorted(elves, reverse=True)[:3])
    result2 = sum(topThree)
    print("Sum of top three:",result2)
