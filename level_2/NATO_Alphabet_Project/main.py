import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")


df = pd.DataFrame(data)
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
phonetic_word_list = [phonetic_dict[letter] for letter in word]
print(phonetic_word_list)
