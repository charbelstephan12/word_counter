f = open("C:\\Users\\Charbel\\Desktop\\project\\demofile.txt")
txt=f.read().replace('\n',' ')
txt=txt.upper()
txt_split=txt.split()
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet=alphabet.upper()
alphabet=[*alphabet]
x=[*txt]

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

def letter_by_letter():
    for i in range(0,26):
        z=alphabet[i]
        print(z,":",countX(x,z))

def print_letter_count():
    print("Letter count:",len(txt))
def print_word_count():
    print("Word count :",len(txt_split))

f.close()