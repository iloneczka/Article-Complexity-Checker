### 🔴 Ćwiczenie

# Popraw program M01L13. W tym programie sprawdzaliśmy złożoność tekstów licząc jaka jest średnia długość słów. Na tamtym etapie nie znaliśmy metody jak wyliczyć tą wielkość dokładnie, bez spacji, znaków interpunkcyjnych czy też pomijając liczby w tekście.

# Popraw kod tak, aby nie zliczał spacji ani znaków interpunkcyjnych. Dodatkowo, jeśli w tekście pojawiają się liczby, to również nie bierz ich pod uwagę.

import string

PUNCTUATION= string.punctuation

def remove_punctuation(text):
    for char in PUNCTUATION:
        text= text.replace(char, "")
    return text

def calculate_average_word_length(text):
    words = remove_punctuation(text).split()
    without_numbers= [w for w in words if not w.isnumeric()]
    length= [len(w) for w in without_numbers]
    average= sum(length) / len(length)
    return average

def main():
    user_text= input("Write your text: ")

    average_lenght= calculate_average_word_length(user_text)
    print("Średnia długość słów podanego tekstu wynosi:", average_lenght)

if __name__ == "__main__":
    main()
