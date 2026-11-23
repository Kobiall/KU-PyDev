# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej
bok_a = float(input("Podaj długość boku a: "))
bok_b = float(input("Podaj długość boku b: "))
bok_c = float(input("Podaj długość boku c: "))
if bok_a >= bok_b + bok_c or bok_b >= bok_a + bok_c or bok_c >= bok_a + bok_b:
    print("Nie da się zbudować trójkąta")
elif bok_a == bok_b and bok_b == bok_c:
    print("równoboczny")
elif bok_a == bok_b or bok_a == bok_c or bok_b == bok_c:
    print("równoramienny")
else:
    print("różnoboczny")
if bok_a < bok_b + bok_c and bok_b < bok_a + bok_c and bok_c < bok_a + bok_b:
    boki = sorted([bok_a, bok_b, bok_c])
    if abs(boki[0]**2 + boki[1]**2 - boki[2]**2) < 1e-9:
        print("prostokątny")