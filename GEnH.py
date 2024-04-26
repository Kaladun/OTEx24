import random

def has_punctuation(txt):
    if txt.find(".") != -1 or txt.find("!") != -1 or txt.find("?") != -1:
        return True
    return False


def new_sentence():
    random.shuffle(start_list)
    sentence = [start_list[0]]
    i = 0
    while i < 50:
        random.shuffle(dictionary[sentence[i]])
        sentence.append(dictionary[sentence[i]][0])
        i += 1
        if has_punctuation(sentence[i]):
            break
    st = ""
    for w in sentence:
        st = st + w + " "
    return st


def analyze_dictionary(d_key):
    print(" ")
    print("WORD FREQUENCY AFTER " + str(d_key))
    d_list = dictionary[d_key].copy()
    c = len(d_list)
    while len(d_list) > 0:
        w = d_list[0]
        cw = d_list.count(w)

        print(str(w) + " :  " + str(round(cw/c*100, 1)) + "%   (" + str(cw) + ")")
        while w in d_list:
            d_list.remove(w)


def make_poem(n):
    print(" ")
    for i in range(0, n):
        print(new_sentence())
    input()


start_list = []
dictionary = {}

last = ""
start = True
with open("Green Eggs and Ham.txt", 'r') as file:
    for line in file:
        for word in line.split():
            if start:
                start_list.append(word)
                start = False
            if last != "":
                if last not in dictionary:
                    dictionary[last] = []
                dictionary[last].append(word)
            start = has_punctuation(word)
            last = word
file.close()

while True:
    print("GE&H Markov Generator:")
    print("1 to generate poem")
    print("2 to see frequencies")
    inp = input()
    if inp.count("1") > 0:
        make_poem(random.randint(3, 9))
    elif inp.count("2") > 0:
        print("WORD TO ANALYZE:")
        k = input().upper()
        if k not in dictionary:
            print(str(k) + " is not in dictionary")
        else:
            analyze_dictionary(k)
            input()