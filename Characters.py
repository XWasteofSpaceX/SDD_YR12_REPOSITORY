characters = []
repeats = 0
total = 0
end = False
while not end:
    character = input("Enter a character: ")
    if not character:
        break
    elif character not in characters:
        characters.append(character)
        total += 1
    else:
        repeats += 1
print(f'You named {total} Characters(s)')
print(f'You repeated {repeats} time(s)')
