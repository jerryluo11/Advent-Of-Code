with open("puzzleinput.txt") as file:
    data = file.read().strip().split("\n")

ans = 0

for line in data:
    id, result = line.split(": ")
    redMax = 0
    greenMax = 0
    blueMax = 0

    for game in result.split("; "):
        for eachCube in game.split(", "):
            num, color = eachCube.split(" ")
            num = int(num)
            if color == "red" and num > redMax:
                redMax = num
            if color == "green" and num > greenMax:
                greenMax = num
            if color == "blue" and num > blueMax:
                blueMax = num
    power = redMax * greenMax * blueMax
    ans += power
print(ans)
            



