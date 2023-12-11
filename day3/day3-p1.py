with open("puzzle_input.txt") as file:
    lines = file.read().strip().split("\n")

"""
iterate through, get a number, check all the positions for a symbol
"""
n = len(lines)
m = len(lines[0])

def isSymbol(i, j):
    if not (0 <= i < n and 0 <= j < m):
        return False
    return lines[i][j] != "." and not lines[i][j].isdigit()

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
        if isSymbol(i, start - 1) or isSymbol(i, j):
            ans += num
            continue
        for k in range(start - 1, j + 1):
            if isSymbol(i - 1, k) or isSymbol(i + 1, k):
                ans += num
                break
print(ans)

        



