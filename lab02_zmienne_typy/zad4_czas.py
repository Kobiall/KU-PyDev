# Lab 02 – Zadanie 4 (★): Sekundy na godziny, minuty i sekundy
#
# Program wczytuje liczbę sekund (int) i wypisuje ją DOKŁADNIE w formacie:
#     1 h 2 min 5 s
# (dla 3725 sekund).
#
# Wskazówki:
#   - int(input(...)) – konwersja tekstu na liczbę całkowitą
#   - // dzielenie całkowite, % reszta z dzielenia
#   - 1 h = 3600 s, 1 min = 60 s

# TODO: Twój kod poniżej
liczba_sekund = int(input("Podaj liczbę sekund: "))
h = liczba_sekund // 3600
min = (liczba_sekund % 3600) // 60
s = liczba_sekund % 60
print(f"{h} h {min} min {s} s")


