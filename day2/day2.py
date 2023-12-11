numValid = 0
with open("puzzleinput.txt", "r") as file:
    for line in file:
        valid = True
        for i, c in enumerate(line):
            if c == ';' or ',':
                if line[i - 4 : i] == "blue":
                    if int(line[i - 7: i - 5]) > 14:
                        valid = False
                elif line[i - 3: i] == "red":
                    if int(line[i - 6: i - 4]) > 12:
                        valid = False
                elif line[i - 5: i] == "green":
                    if int(line[i - 8: i - 6]) > 13:
                        valid = False
        if valid:
            if line[6] == ":":
                numValid+=int(line[5:6])
            else:
                numValid+=int(line[5:7])
print(numValid)


                    
             