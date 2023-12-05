### Part 1

with open("input.txt") as input:
    soln = 0
    lines = []
    for row in input:
        lines.append(row.strip())
    print(lines)
    partStart = []
    def find_part(string, index, num):
        part = string[index][num] # The starting point of part is just the found digit
        if (string[index][num + 1]).isdigit(): # This checks the character directly to the right of the found digit and adds to the partID
            part += string[index][num + 1]
            if (string[index][num + 2]).isdigit(): # If the character directly to the right of the found digit is a digit, this checks the character to the right of that
                part += string[index][num + 2]
        if (string[index][num - 1]).isdigit(): # This checks the character directly to the left of the found digit and adds to the partID
            part = string[index][num-1] + part
            if (string[index][num - 2]).isdigit(): # If the character directly to the left of the found digit is a digit, this checks the character to the left of that
                part = string[index][num - 2] + part
                if (str(index) + "-" + str(num - 2)) not in partStart: # Checks if the part isn't already added
                    partStart.append(str(index) + "-" + str(num - 2))
                    return int(part)
                else:
                    return 0 # Ask Will if I need to do this
            else:
                if (str(index) + "-" + str(num - 1)) not in partStart: # Checks if the part isn't already added
                    partStart.append(str(index) + "-" + str(num - 1))
                    return int(part)
                else:
                    return 0
        if (string[index][num - 1]).isdigit() == False: 
            if (str(index) + "-" + str(num)) not in partStart: # Checks if the part isn't already added
                partStart.append(str(index) + "-" + str(num))
                return int(part)
            else:
                return 0
    for idx, line in enumerate(lines):
        for i in range(len(line)):
            char = line[i]
            if char.isdigit(): # Checks if character in the line is a number
                continue
            if char == ".": # Check is the character in the line is a .
                continue
            else: # Runs this if a special character is found, checks all eight characters that surround the special character to look for unique parts
                print(char)
                if i != 0: # Check to see if it it's not the first character in a line
                    if (lines[idx][i - 1]).isdigit(): #4 Checks if character directly left is a digit
                        soln += find_part(lines, (idx), (i - 1))
                    if idx != 0: # Check to see if this is not the first line
                        if (lines[idx - 1][i - 1]).isdigit(): #1 Checks if charcter up and to the left is a digit
                            soln += find_part(lines, (idx - 1), (i - 1))
                    if idx != (len(lines) - 1): # Check to see if this is not the last line
                        if (lines[idx + 1][i - 1]).isdigit(): #6 Checks if character down and to the left is a digit
                            soln += find_part(lines, (idx + 1), (i - 1))

                if idx != len(lines) - 1: # Check to see if this is not the last line
                    if (lines[idx + 1][i]).isdigit(): #7 Checks if character directly below is a digit
                        soln += find_part(lines, (idx + 1), (i))
                    if i != len(line) - 1: # Check to see if this is not the last character in a line
                        if (lines[idx + 1][i + 1]).isdigit(): #8 Checks if character down and to the right is a digit
                            soln += find_part(lines, (idx + 1), (i + 1))

                if i != len(line) - 1: # Check to see if this is not the last character in a line
                    if (lines[idx][i + 1]).isdigit(): #5 Checks if character directly right is a digit
                        soln += find_part(lines, (idx), (i + 1))
                    if idx != 0: # Check to see if this is not the first line
                        if (lines[idx - 1][i + 1]).isdigit(): #3 Checks if character up and to the right is a digit
                            soln += find_part(lines, (idx - 1), (i + 1))

                if idx != 0: # Check to see if this is not the first line
                    if (lines[idx - 1][i]).isdigit(): #2 Checks if character directly above is a digit
                        soln += find_part(lines, (idx - 1), (i))
    print(partStart)
    print(soln)
            # partStart.append(str(idx) + str(i))
            # print(char)
    # print(partStart)
