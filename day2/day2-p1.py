with open("puzzleinput.txt") as file:
    data = file.read().strip().split("\n")

ans = 0

for line in data:
    game, result = line.split(": ")
    id = int(game.split(" ")[1])

    valid = True
    for game in result.split("; "):
        for eachCube in game.split(", "):
            num, color = eachCube.split(" ")
            num = int(num)
            if color == "red" and num > 12:
                valid = False
            if color == "green" and num > 13:
                valid = False
            if color == "blue" and num > 14:
                valid = False
    if valid:
        ans += id

print(ans)
            



