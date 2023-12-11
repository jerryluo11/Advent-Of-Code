with open("puzzle_input.txt") as file:
    lines = file.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

data = {}
def isGear(i, j, num):
    if not (0 <= i < n and 0 <= j < m):
        return False
    if lines[i][j] == "*":
        if (i, j) not in data:
            data[(i,j)] = [num]
        else:
            data[(i,j)].append(num)
    return False

ans = 0
for i, line in enumerate(lines):
    start = 0

    j = 0

    while j < m:
        num = ""
        start = j
        while j < m and line[j].isdigit():
            num+=line[j]
            j += 1
        if num == "":
            j += 1
            continue
        num = int(num)

        #Looking for a symbol
        isGear(i, start - 1, num) or isGear(i, j, num)
        for k in range(start - 1, j + 1):
            isGear(i - 1, k, num) or isGear(i + 1, k, num)

for key, value in data.items():
    if len(value) == 2:
        ans += (value[0] * value[1])
print("program", ans)
        



