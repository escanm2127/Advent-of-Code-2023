### Part 1

with open("input.txt") as input:
    soln = 0
    for line in input:
        splitLine = line.split()
        for i in range(2, len(splitLine), 2):
            if int(splitLine[i]) >= 15: # if anything is greater than 15 then its automatically bad
                break
            if int(splitLine[i]) <= 12:
                if i+2 == len(splitLine):
                    gameNum = int(splitLine[1][:-1]) # gets the game number
                    soln += gameNum
                continue
            if int(splitLine[i]) > 12 and "red" in splitLine[i+1]:
                break
            if int(splitLine[i]) > 13 and "green" in splitLine[i+1]:
                break
            if i+2 == len(splitLine):
                gameNum = int(splitLine[1][:-1]) # gets the game number
                soln += gameNum
            
    print(soln)    


### Part 2

with open("input.txt") as input:
    soln = 0
    for line in input:
        splitLine = line.split()
        for i in range(2, len(splitLine), 2):
            pass