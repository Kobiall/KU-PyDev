# Lab 02 – Zadanie 2 (★): Konwerter temperatury
#
# 1. Wczytaj temperaturę w stopniach Celsjusza i wypisz ją w Fahrenheitach:
#        F = C * 9 / 5 + 32
# 2. Wczytaj temperaturę w stopniach Fahrenheita i wypisz ją w Celsjuszach:
#        C = (F - 32) * 5 / 9
#
# Przykład: 37 °C = 98.6 °F,  212 °F = 100.0 °C
# Wyniki zaokrąglij do 1 miejsca po przecinku: f"{x:.1f}"

# TODO: Twój kod poniżej
celcjusza = float(input("Podaj tempeaturę w celcjuszach: "))
fahrenhita = celcjusza * 9 / 5 + 32
print(f"Temperatura w F: {fahrenhita:.1f}")
fahrenhita = float(input("Podaj temperaturę w Fahrenhitach: "))
celcjusza = (fahrenhita - 32) * 5 / 9
print(f"Temperatura w C: {celcjusza:.1f}")
