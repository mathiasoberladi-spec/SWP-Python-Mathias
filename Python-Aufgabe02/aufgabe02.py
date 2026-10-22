KLEINSTE_ZAHL = 1
GROESSTE_ZAHL = 10
TEILER_GERADE = 2

SCHLECHTESTE_POSITIVE_NOTE = 4
NOTEN = [1, 3, 5, 2, 4, 5, 1]

ALTER_VOLLJAEHRIG = 18
PERSONEN = {"Anna": 17, "Ben": 19, "Clara": 18, "David": 15}


# List-Comprehension: [wert_wenn_wahr if bedingung else wert_wenn_falsch for element in sammlung]
def erstelle_gerade_ungerade_liste():
    return ["gerade" if zahl % TEILER_GERADE == 0 else "ungerade"
            for zahl in range(KLEINSTE_ZAHL, GROESSTE_ZAHL + 1)]


# Set-Comprehension: wie die Liste, aber mit {} -> doppelte Werte fallen weg
def erstelle_ergebnis_menge(noten):
    return {"bestanden" if note <= SCHLECHTESTE_POSITIVE_NOTE else "nicht bestanden"
            for note in noten}


# Dict-Comprehension: {schluessel: wert_wenn_wahr if bedingung else wert_wenn_falsch for ...}
def erstelle_volljaehrigkeit_dictionary(personen):
    return {name: "volljährig" if alter >= ALTER_VOLLJAEHRIG else "minderjährig"
            for name, alter in personen.items()}


def gib_ergebnis_aus(beschreibung, ergebnis):
    print(beschreibung, ergebnis)


def main():
    gib_ergebnis_aus("List-Comprehension:", erstelle_gerade_ungerade_liste())
    gib_ergebnis_aus("Set-Comprehension: ", erstelle_ergebnis_menge(NOTEN))
    gib_ergebnis_aus("Dict-Comprehension:", erstelle_volljaehrigkeit_dictionary(PERSONEN))


if __name__ == "__main__":
    main()
