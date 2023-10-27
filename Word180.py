array = []

while True:
    line = input("Line: ")
    if not line:
        break
    array.append(line)

def reverse(line):
    words = line.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

for line in array:
    rline = reverse(line)
    print(rline)
