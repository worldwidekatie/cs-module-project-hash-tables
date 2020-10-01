import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    text = f.read()
    # text = text.replace("\n\n", " \n\n ")
    # text = text.replace("\n", " \n ")
    # text = text.replace("--", " -- ")
    # text = text.replace('"', ' " ')
    text = text.split(" ")
    words = []
    for i in text:
        if i not in words and len(i) >= 1:
            words.append(i)
    start = []
    end = []
    punct = [".", "!", "?", '."', '!"', '?"']
    caps = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U','G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z', '"E', '"T', '"A', '"O', '"H', '"N', '"R', '"I', '"S', '"D', '"L', '"W', '"U', '"G', '"F', '"B', '"M', '"Y', '"C', '"P', '"K', '"V', '"Q', '"J', '"X', '"Z']
    for i in words:
        if len(i) >= 1:
            if i[0] in caps:
                start.append(i)
            if i[-1] in punct:
                end.append(i)

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
    word1 = random.choice(start)
    sentence += word1 + " "
    word2 = random.choice(follows[word1])
    sentence += word2 + " "
    word = random.choice(follows[word2])
    # To fix this dumb error?
    var = " " + word
    while var[-1] not in punct:
        next_word = random.choice(follows[word])
        sentence += next_word + " "
        word = next_word
        var = " " + word
    print(sentence)
    print("------------------------")
