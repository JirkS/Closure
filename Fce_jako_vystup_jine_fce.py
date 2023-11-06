def formatuj_prijimeni_prvni(jmeno: str, prijmeni: str):
    return prijmeni + " " +jmeno


def formatuj_monogram(jmeno: str, prijmeni: str):
    return jmeno[0] + "." + prijmeni[0] + "."


def vyber_formatovaci_funkci(delka):
    if delka < 4:
        return formatuj_monogram
    else:
        return formatuj_prijimeni_prvni


try:
    formatovac = vyber_formatovaci_funkci(3)
    print(formatovac("Jan", "Novak"))
    formatovac = vyber_formatovaci_funkci(155)
    print(formatovac("Jan", "Novak"))
except Exception as e:
    print(e)
