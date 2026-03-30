import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}


def spell(word):
    try:
        nato_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        return False
    else:
        print(nato_word)


word = input("What is the word?: ").upper()

while spell(word) is False:
    word = input("What is the word?: ").upper()