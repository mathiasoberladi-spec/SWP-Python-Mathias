import random

def lottoziehung():
    zahlen = list(range(1, 46))
    bereich = len(zahlen)

    for _ in range(6):
        index = random.randrange(bereich)
        letzter = bereich - 1
        zahlen[index], zahlen[letzter] = zahlen[letzter], zahlen[index]
        bereich -= 1

    return zahlen[bereich:]

def statistik(gezogene_zahlen, haeufigkeit):
    for zahl in gezogene_zahlen:
        haeufigkeit[zahl] += 1

def main():
    print("Gezogene Zahlen:", sorted(lottoziehung()))

    for anzahl in (1000, 10000, 100000):
        haeufigkeit = {zahl: 0 for zahl in range(1, 46)}
        for _ in range(anzahl):
            ziehung = lottoziehung()
            statistik(ziehung, haeufigkeit)

        print(f"\nHäufigkeiten nach {anzahl} Ziehungen:")
        for zahl, count in haeufigkeit.items():
            print(f"  {zahl:2d}: {count}")

main()