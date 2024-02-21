import string

def countX(lst, x):
    return lst.count(x)


def letter_by_letter():
    for char in alphabet:
        count = countX(txt, char)
        if count > 0 and char!=" ":
            print(char, ":", count)
        elif count>0 and char==" ":
            print("space :", count)

def print_letter_count():
    print("Letter count:", len(txt))

def print_word_count():
    print("Word count:", len(txt_split))

with open("demo.file.txt") as f:
    txt = f.read().replace('\n', ' ')
    txt_split = txt.split()

alphabet = string.printable