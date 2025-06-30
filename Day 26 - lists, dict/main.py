import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
translated = {row.letter:row.code for (index,row) in data.iterrows()}

def gen_phonetic():
    user_input = input("What is your word?: ").upper()
    try:
        output = [translated[letter] for letter in user_input]
    except KeyError:
        print("Input invalid. Provide only letters from the alphabet")
        gen_phonetic()
    else:
        print(output)
gen_phonetic()