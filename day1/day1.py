#part 1
'''
total_sum = 0
with open("puzzleinput.txt", "r") as file:
    for line in file:
        first_dig = 0
        last_dig = 0
        no_digit_read = True
        for char in line:
            if (ord(char) >= 48 and ord(char) <= 57):
                if no_digit_read:
                    first_dig = ord(char) - 48
                    no_digit_read = False
                last_dig = ord(char) - 48
        line_sum = first_dig * 10 + last_dig
        total_sum += line_sum


print("Total sum", total_sum)
'''
#part 2

wordToInt = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
}

with open("puzzleinput.txt", "r") as file:
    for line in file:



        first_dig = 0
        last_dig = 0
        no_digit_read = True
        for char in line:
            if (ord(char) >= 48 and ord(char) <= 57):
                if no_digit_read:
                    first_dig = ord(char) - 48
                    no_digit_read = False
                last_dig = ord(char) - 48
        line_sum = first_dig * 10 + last_dig
        total_sum += line_sum


