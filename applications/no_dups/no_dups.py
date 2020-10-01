def no_dups(s):
    words = [(s.split(" ")[0])]
    string = (s.split(" ")[0])
    for i in s.split(" "):
        if i not in words:
            words.append(i)
            string += (" " + i)
    return string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))