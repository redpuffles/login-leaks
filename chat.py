sections = []

f = open("sections.txt", "r")

for line in f:
    sections.append(line.strip())

f.close()

letters = ['>', 'W', '_', '(', '^', '}', '$', 'z', 'q', '9', 'A', '-', 'R', '*', '2', '<', 'f', 'e', '6', '&', 'Z', 'd', '{', '!', 'n', 'L', ')']

letters.sort()

print(letters)
print(len(letters))
print()

password = {}
i = 0

for letter in letters:
    before = []
    after = []
    for section in sections:
        if letter in section:
            if letter == section[0]:
                if section[1] not in after:
                    after.append(section[1])
                if section[2] not in after:
                    after.append(section[2])
            elif letter == section[1]:
                if section[0] not in before:
                    before.append(section[0])
                if section[2] not in after:
                    after.append(section[2])
            elif letter == section[2]:
                if section[0] not in before:
                    before.append(section[0])
                if section[1] not in before:
                    before.append(section[1])
    print(i, letter, len(before), len(after))
    password[len(before)] = letter
    i = i + 1
p = []
for k in sorted(password):
    print(k, password[k])
    p.append(password[k])

print("".join(p))
