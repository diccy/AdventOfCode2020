with open("d2.txt", "r") as f:
    content = f.read().splitlines()

bg1 = 0
bg2 = 0
for line in content:
    s = line.split(" ")
    numbers = s[0].split("-")
    min = int(numbers[0])
    max = int(numbers[1])
    letter = s[1][0]
    pwrd = s[2]
    letter_count = 0
    letter_found = 0
    i = 0
    for c in pwrd:
        i += 1
        if c == letter:
            letter_count += 1
            if i == min or i == max:
                letter_found += 1
    if min <= letter_count and letter_count <= max:
        bg1 += 1
    if letter_found == 1:
        bg2 += 1

print("Bons gaulois 1: ", bg1)
print("Bons gaulois 2: ", bg2)
