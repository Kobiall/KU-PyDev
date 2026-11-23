# Lab 03 – Zadanie 2 (★): Kalkulator z wyborem działania
#
# Program wczytuje kolejno: liczbę, operator (+, -, *, /) i drugą liczbę,
# a potem wypisuje wynik, np.:  8.0 * 2.0 = 16.0
#
# Obsłuż przypadki szczególne instrukcją if:
#   - dzielenie przez zero  -> "Nie można dzielić przez zero"
#   - inny operator         -> "Nieznany operator"

# TODO: Twój kod poniżej
liczba_a = float(input("Podaj pierwszą liczbę: "))
operator = input("Podaj operator (+, -, *, /): ")
liczba_b = float(input("Podaj drugą liczbę: "))
if operator == "+":
    wynik = liczba_a + liczba_b
    print(f"{liczba_a} + {liczba_b} = {wynik:.1f}")
elif operator == "-":
    wynik = liczba_a - liczba_b
    print(f"{liczba_a} - {liczba_b} = {wynik:.1f}")
elif operator == "*":
    wynik = liczba_a * liczba_b
    print(f"{liczba_a} * {liczba_b} = {wynik:.1f}")
elif operator == "/":
    if liczba_b == 0:
        print("Nie można dzielić przez zero")
    else:
        wynik = liczba_a / liczba_b
        print(f"{liczba_a} / {liczba_b} = {wynik:.1f}")
else:
    print("Nieznany operator")