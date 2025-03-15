# Enumerate () - zwraca obiekt będący sekwencją, iteratorem bądź innym obiektem, który obsługuje iteracje.
# https://docs.python.org/3/library/functions.html#enumerate

# Random - generuje losową liczbę dla różnych rozkładów.
# https://docs.python.org/3/library/random.html#module-random

# ValueError - występuje, gdy operacja lub funkcja otrzymuje argument o poprawnym typie, ale nieodpowiedniej wartości, a sytuacja nie jest opisana przez bardziej precyzyjny wyjątek.
# https://docs.python.org/3/library/exceptions.html#ValueError


# importujemy moduł random do wykorzystania funkcji random.choice()
import random

# tworzymy dwie listy
a = [1, 2, 3, 4]
b = ['pies', 'kot', 'chomik', 'żółw']

# łączymy listy za pomocą funckji zip()
zipped_lists = list(zip(a, b))
print("Połączone listy:", zipped_lists)

# wykorzystujemy funkcję choice z modułu random
random_element = random.choice(a) # losowy wybór z listy a
print("Losowy element z listy a:", random_element)

# obsługa wyjątku try-except
def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Błąd: Indeks poza zakresem listy"
    
# test obsługi wyjątku
print(get_element(a, 7)) # próba uzyskania elementu spoza zakresu

# komentarze i linki do dokumentacji:
# zip() - Zwraca obiekt iteratora, który można przekonwertować na listę lub krotkę. 
# https://docs.python.org/3/library/functions.html#zip

# random.choice() - zwraca losowy element z podanej sekwencji (np. listy, krotki, stringa). Jeśli lista jest pusta, rzuca wyjątek. 
# https://docs.python.org/3/library/random.html#random.choice