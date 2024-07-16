import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for index, row in file.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)

    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
        generate_phonetic()


generate_phonetic()

