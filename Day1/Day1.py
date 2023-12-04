with open("inputDay1.txt") as input:
    soln = 0
    digits_list = {
        "one": "one1one", 
        "two": "two2two", 
        "three": "three3three",
        "four" : "four4four",
        "five" : "five5five",
        "six" : "six6six",
        "seven" : "seven7seven",
        "eight" : "eight8eight",
        "nine" : "nine9nine"
    }
    for line in input:
        new_line = line
        for key, value in digits_list.items():
            new_line = new_line.replace(key, value)
        x = []
        for char in new_line:
            if str.isdigit(char):
                x.append(char)
        strsoln = x[0] + x[-1]
        print(strsoln)
        soln += int(strsoln)
    print(soln)



# def check_word_number(string_to_check):
#     pass
