import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter : row.code for (index,row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input ("Enter a word: ").upper()
result = [nato_dict[char] for char in word]
print(result)
