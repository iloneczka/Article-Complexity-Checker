### 🔴 Projekt

# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy piszą teksty proste i łatwe w zrozumieniu. Policz jaka jest średnia długość słów i wyświetl rezultat.

import re
text= input("Wpisz tekst: ")
number_letters= len(re.findall("[a-zA-Z0-9]",text))  #ilość wszystkich liter bez spacji i znaków specjalnych.
number_words= len(text.split())  #ilosc slów
average = number_letters / number_words
print("Słowa w Twoim tekście mają średnio", average, "znaków")
