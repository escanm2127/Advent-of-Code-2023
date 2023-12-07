### Part 1

# with open("input.txt") as input:
#     soln = 0
#     for line in input:
#         splitLine = line.split()
#         splitLine = splitLine[2:]
#         winNums = []
#         myNums = []
#         points = 0
#         for i in range(len(splitLine)):
#             if splitLine[i] != "|":
#                 winNums.append(splitLine[i])
#             else:
#                 for x in range(i + 1, len(splitLine)):
#                     myNums.append(splitLine[x])
#                 break
#         for i in range(len(myNums)):
#             if myNums[i] in winNums:
#                 if points != 0:
#                     points *= 2
#                 else:
#                     points = 1
#         soln += points
#     print(soln)


### Part 2

with open("input.txt") as input:
    soln = 0
    cards = {}
    cardNum = 0
    for line in input:
        cardNum += 1
        splitLine = line.split()
        splitLine = splitLine[2:]
        winNums = []
        myNums = []
        points = 0

        if cardNum not in cards.keys():
            cards[cardNum] = 1
        else:
            cards[cardNum] += 1
        
        for i in range(len(splitLine)):
            if splitLine[i] != "|":
                winNums.append(splitLine[i])
            else:
                for x in range(i + 1, len(splitLine)):
                    myNums.append(splitLine[x])
                break
        match = 0
        for i in range(len(myNums)):
            if myNums[i] in winNums:
                match += 1
        
         
        if match != 0:
            for x in range(1, match + 1):
                if (cardNum + x) not in cards.keys():
                    cards[(cardNum + x)] = (1 * cards[cardNum])
                else:
                    cards[(cardNum + x)] += (1 * cards[cardNum])

    soln = sum(cards.values())
    print(soln)