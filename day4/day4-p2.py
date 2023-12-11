with open("input.txt") as file:
    data = file.read().strip().split("\n")

pile = 0

numOfLines = len(data)
database = [1] * numOfLines
for line in data:
    matches = 0
    cards, numbers = line.split(":")
    id = cards.split()[1]
    id = int(id)
    winning, our = numbers.split("|")
    winningArray = winning.split()
    ourArray = our.split()

    for i in ourArray:
        for j in winningArray:
            if i == j:
                matches += 1
    for i in range(1, matches + 1):
        if ((id - 1 + i) < numOfLines):
            database[id - 1 + i] += database[id - 1]
for num in database:
    pile += num
print(pile)