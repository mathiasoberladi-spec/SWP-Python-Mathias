import random

def lottoziehung():
    urne = list(range(1, 46))      # Zahlen von 1-45
    gezogen = []
    for _ in range(6):
        index = random.randrange(len(urne))   # genau 1 Zufallsaufruf pro Zahl
        gezogen.append(urne.pop(index))
    return gezogen

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