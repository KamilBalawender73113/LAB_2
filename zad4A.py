bramki=float(input("Podaj liczbę strzelonych bramek przez drużyne: "))
bonus= bramki * 10 #każdy gol jest liczony jako 10 punktów
if bramki>10:
    bonus= bonus + 10 #za strzelenie 10 goli przyznaje się 10 dodatkowych punktów
elif bramki>=5 and bramki<11:
    bonus= bonus + 5 #za strzelenie 5 goli przyznaje się 5 dodatkowych punktów
print(f"Liczba zdobytych punktów:{bonus}")