trash = raw_input()
plain = raw_input()
k = int(raw_input())
cipher = ''
for c in plain:
    if 122 >= ord(c) > 96:
        cipher += chr((ord(c) + k - 97) % 26 + 97)
    elif 90 >= ord(c) > 64:
        cipher += chr((ord(c) + k - 65) % 26 + 65)
    else:
        cipher += c
print cipher