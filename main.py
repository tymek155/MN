import math
def file_read(nazwa, tab1, tab2):
    with open(nazwa, "r") as odczyt:
        ilosc = int(odczyt.readline())

        for i in range(ilosc):
            wart1, wart2 = map(float, odczyt.readline().split())
            tab1.append(wart1)
            tab2.append(wart2)

        return ilosc


def interpolacja(ilosc, xi, fxi, punkt):
    wynik = 0

    for i in range(ilosc):
        licznik = 1
        mianownik = 1
        for j in range(ilosc):
            if i != j:
                licznik *=(punkt-xi[j])
                mianownik*=(xi[i]-xi[j])

        wynik+=fxi[i]*(licznik/mianownik)

    return wynik


def main():
    xi = []
    fxi = []
    ilosc_wezlow = file_read("MN.txt", xi, fxi)
    print(f"Liczba węzłów wynosi: {ilosc_wezlow}")
    print(f"Węzły interpolacji: {xi}")
    print(f"Wartości w węzłach: {fxi}")
    punkt = int(input("Podaj punkt w ktorym chcesz policzyc wartosc wielamianu: "))
    print(f"Podany punkt {punkt}")
    print(f"Wartosc wielomianu Lagrange'a w podanym punkcie wynosi {interpolacja(ilosc_wezlow, xi, fxi, punkt)}")

    ilosc_wezlow = 0
    xi1=[27,64,125,216]
    fxi1=[]
    for i in xi1:
        fxi1.append(math.pow(i, 1/3))
        ilosc_wezlow += 1
    print(f"Liczba węzłów wynosi: {ilosc_wezlow}")
    print(f"Węzły interpolacji: {xi1}")
    print(f"Wartości w węzłach: {fxi1}")
    punkt = int(input("Podaj punkt w ktorym chcesz policzyc wartosc wielamianu: "))
    print(f"Podany punkt {punkt}")
    print(f"Wartosc wielomianu Lagrange'a w podanym punkcie wynosi {interpolacja(ilosc_wezlow, xi1, fxi1, punkt)}")


if __name__ == '__main__':
    main()
