# zadaca 1
# Da se napise funkcija koja za vnesena lista i vnesen broj ke gi ispecati
# indeksite na dva broevi taka sto nivniot zbir ke bide ednakov na vneseniot broj.

def najdi_indeks(broj, lista):
    broevi_indeksi = {}

    for indeks, vrednost in enumerate(lista):
        razlika = broj - vrednost

        if razlika in broevi_indeksi:
            return broevi_indeksi[razlika] + 1, indeks + 1
        else:
            broevi_indeksi[vrednost] = indeks

    return None

vnesen_broj = int(input("Vnesete broj: "))
vnesena_lista = [int(x) for x in input("Vnesete lista od broevi (odvoeni so prazno mesto): ").split()]

rezultat = najdi_indeks(vnesen_broj, vnesena_lista)

if rezultat:
    print(f"Indeksite na dva broevi koi davaat zbir {vnesen_broj} se: {rezultat[0]} i {rezultat[1]}")
else:
    print("Ne se najdeni dva broevi so takov zbir.")



# zadaca 2
# Da se napise funkcija koja za vnesena lista so elementi ke ispecati dali e toa lista so palindromi.

def palindrom(lista):
    for i in lista:
        if i == i[::-1]:
            print(f"{i} e palindrom")
        else:
            print(f"{i} ne e palindrom")

lista = []
dolzina_lista = int(input("Vnesi dolzina na lista: "))
for i in range(0, dolzina_lista):
    elem = input()
    lista.append(elem)
print(lista)

palindrom(lista)

# zadaca 3
# Da se napise funkcija koja za vnesena recenica ke ja isprinta dolzinata na posledniot zbor.

def dolzina_posleden_zbor(recenica):
    zbor = recenica.split()
    posleden_zbor = zbor[-1]
    dolzina = len(posleden_zbor)
    return dolzina

rrecenica = input("Vnesi recenica: ")
dolzina_zbor = dolzina_posleden_zbor(rrecenica)
print("Dolzinata na posledniot zbor e: ", dolzina_zbor)

# zadaca 4
# Da se napise funkcija koja za vnesen broj N1 i broj N2 ke pecati dali e N1 ednakov na N2 na nekoj stepen.
def stepen(N1, N2):
    if N1 == N2:
        return True
    elif N1 < N2:
        return False
    else:
        i = 2
        while i <= N1:
            if N1**(1/i) == N2:
                return True
            i += 1
        return False

N1 = int(input("Vnesi go prviot broj: "))
N2 = int(input("Vnesi go vtoriot broj: "))

if stepen(N1, N2):
    print(f"{N1} e ednakov so {N2} na nekoj stepen.")
else:
    print(f"{N1} ne e ednakov so {N2} na nitu eden stepen.")

# zadaca 5
# Imame zadadeno mnozestvo so zborovi so ednakva dolzina, i imame zadadeno poceten (start) i kraen zbor (kraj).
# Da se najde najkratkiot pat (N) pomegju pocetniot i krajniot zbor, dokolku takov pat postoi,
# taka sto sosednite zborovi vo mnozestvoto se razlikuvaat megju sebe za 1 bukva.
# Da se ispecatat ovie zborovi na sledniot nacin
# start--->zbor1_1--->zbor2_2--->...--->zborN_N--->kraj .