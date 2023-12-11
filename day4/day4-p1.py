with open("input.txt") as file:
    data = file.read().strip().split("\n")

pile = 0
for line in data:
    game = 0
    cards, numbers = line.split(":")
    winning, our = numbers.split("|")
    winningArray = winning.split()
    ourArray = our.split()
    for i in ourArray:
        for j in winningArray:
            if i == j:
                if game == 0:
                    game += 1
                else:
                    game *= 2
    pile += game
    
print(pile)