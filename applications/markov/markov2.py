import random

"""I wanted to see what would happen if I went by characters
instead of words like when we did text generation with LSTM models.
It didn't go very well. I don't think it's enough data for that..."""

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    text = f.read()
    chars = []
    for i in text:
        for char in i:
            if char not in chars:
                chars.append(char)
    start = ['T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'Q', 'J', '"']
    end = [".", "!", "?"]

# TODO: analyze which words can follow other words
follows = {}

for i in range(0, len(text)-1):
    if text[i] not in follows:
        follows[text[i]] = []
        follows[text[i]].append(text[i+1])
    else:
        follows[text[i]].append(text[i+1])

# TODO: construct 5 random sentences
# Your code here

for i in range(5):
    sentence = ""
    char = random.choice(start)
    while char not in end:
        sentence += char
        char = random.choice(follows[char])
    print(sentence)
    print("------------------------------")


