with open("input.txt") as input:
    soln = 0
    for line in input:
        splitLine = line.split()
        splitLine = splitLine[2:]
        winNums = []
        myNums = []
        points = 0
        for i in range(len(splitLine)):
            if splitLine[i] != "|":
                winNums.append(splitLine[i])
            else:
                for x in range(i + 1, len(splitLine)):
                    myNums.append(splitLine[x])
                break
        for i in range(len(myNums)):
            if myNums[i] in winNums:
                if points != 0:
                    points *= 2
                else:
                    points = 1
        soln += points
    print(soln)
