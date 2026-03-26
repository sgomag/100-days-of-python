import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dic = {row.letter:row.code for (index, row) in nato_df.iterrows()}

word = input("What is the word?: ").upper()
print(word)
nato_word = [nato_dic.get(letter) for letter in word]

print(nato_word)