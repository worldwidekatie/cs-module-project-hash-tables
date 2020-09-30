# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
non_chars = [' ', ',', '.', "'", '\n', '"', ';', ':', '-', '?', '!', '—', '(', '1', ')']
frequent = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U','G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
with open("applications/crack_caesar/ciphertext.txt") as file:
    total = 0
    chars = {}
    for line in file:
        for char in line:
            if char not in non_chars and char not in chars:
                chars[char] = 0
            if char not in non_chars:
                chars[char] += 1
                total += 1
    var = {k: v for k, v in sorted(chars.items(), key=lambda item: item[1], reverse=True)}
    
    key = {}
    index = 0
    for i in var:
        key[i] = frequent[index]
        index += 1

with open("applications/crack_caesar/ciphertext.txt") as file:
    for line in file:
        l = ""
        for char in line:
            if char in key:
                l += key[char]
            elif char not in key:
                l += char
        print(l)
