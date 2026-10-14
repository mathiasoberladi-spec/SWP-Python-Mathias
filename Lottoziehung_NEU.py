import random

# Neu Variante der Lottoziehung:
# Ich habe nun die besprochenen Details umgesetzt - Methoden sollten atomar sein,
#       aussagekräftigen Namen besitzen, Eingabe, usw.

KLEINSTE_ZAHL = 1
GROESSTE_ZAHL = 45
ANZAHL_GEZOGENE_ZAHLEN = 6

def erstelle_alle_zahlen():
    return list(range(KLEINSTE_ZAHL, GROESSTE_ZAHL + 1))

def ziehe_lottozahlen():
    zahlen = erstelle_alle_zahlen()
    bereich = len(zahlen)

    for _ in range(ANZAHL_GEZOGENE_ZAHLEN):
        index = random.randrange(bereich)
        bereich = bereich - 1
        zahlen[index], zahlen[bereich] = zahlen[bereich], zahlen[index]

    return zahlen[bereich:]

def gib_lottozahlen_aus(lottozahlen):
    print("Gezogene Zahlen:", sorted(lottozahlen))

def erstelle_leere_statistik():
    statistik = {}
    for zahl in erstelle_alle_zahlen():
        statistik[zahl] = 0
    return statistik

def aktualisiere_statistik(statistik, lottozahlen):
    for zahl in lottozahlen:
        statistik[zahl] += 1

def frage_anzahl_ziehungen():
    return int(input("Wie viele Ziehungen sollen durchgeführt werden? "))

def fuehre_ziehungen_durch(anzahl_ziehungen):
    statistik = erstelle_leere_statistik()
    for _ in range(anzahl_ziehungen):
        aktualisiere_statistik(statistik, ziehe_lottozahlen())
    return statistik

def gib_statistik_aus(statistik, anzahl_ziehungen):
    print("Häufigkeiten nach", anzahl_ziehungen, "Ziehungen:")
    for zahl, haeufigkeit in statistik.items():
        print(zahl, ":", haeufigkeit)

def main():
    gib_lottozahlen_aus(ziehe_lottozahlen())

    anzahl_ziehungen = frage_anzahl_ziehungen()
    statistik = fuehre_ziehungen_durch(anzahl_ziehungen)
    gib_statistik_aus(statistik, anzahl_ziehungen)


if __name__ == "__main__":
    main()
