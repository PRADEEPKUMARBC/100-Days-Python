import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")
# print(data)

phonetic_list = {row.letter:row.code for ( index, row) in data.iterrows() }
print(phonetic_list)

def generate_phonetic():
    word = input("Enter the word : ").upper()
    try:
        output_list = [phonetic_list[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)

generate_phonetic()