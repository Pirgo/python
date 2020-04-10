import random

def hangman(words):
    res = random.choice(words)
    print('Wylosowane slowo ma ' + str(len(res)) +' liter')
    progress = ["_ "] *len(res)
    cnt = 0
    wrongletter = 0
    while cnt < len(res) and wrongletter <= 3:
        letter = input()
        if len(letter)>1 or letter.isdigit() or letter in progress:
            print("Mozna podac tylko jedna litere, cyfry sa rowniez niedozwolone, lub powtorzyles litere ")
        else:
            begin = 0
            while begin <= len(res):
                idx = res.find(letter, begin, len(res))
                if idx>-1:
                    progress[idx] = letter
                    cnt += 1
                    begin = idx+1
                elif idx == -1 and begin == 0:
                    wrongletter += 1
                    break
                else:
                    break
        print("".join(progress), "liczba nietrafionych liter to " + str(wrongletter))
    if wrongletter > 3:
        print("przegrales")
        return
    else:
        print("Wygrales")





words = open("words.txt", "r").read().splitlines()
hangman(words)
