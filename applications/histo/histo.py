# Your code here

non_chars = ['\n', '!', '"', "'", ',', '-', '.', ':', ';', '?']

with open("applications/histo/robin.txt") as file:
    words = {}
    for line in file:
        l = line.lower()
        for i in non_chars:
            l = l.replace(i, "")
        #lines.append(l)
        l = l.split(" ")
        for i in l:
            if i != "":
                if i not in words:
                    words[i] = 1
                elif i in words:
                    words[i] += 1

frequency = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}

for i in frequency.items():
    x = 17 - len(i[0])
    y = i[0] + (" " * x) + ("#" * i[1])
    print(y)

