# Sa verifice deivizibilitatea unui numar cu 3 si 5 daca este cu 3 si 5 sa returneze 35, daca e cu 3 sa returneze 3 sau daca e cu 5 sa returneze 5
def div_3_5(numar: str):
    if type(numar) == str:
        while numar:
            print(f"din str in caracter pe coloana {numar[0]}")
            numar = numar[1:]

    #Adaugare de caz in care ne confruntam cu boolean
    elif type(numar) == bool:
        if numar == True:
            return False
        else:
            return True

    elif type(numar) == list:
        i = 0
        for n in numar:
            # i=i+1
            i += 1
            print(f"elementul {i} din lista numar este {n} de tipul {type(n)}")
        return f"este lista: {numar}"

    # Control flow
    elif type(numar) == int:
        if numar % 3 == 0 and numar % 5 == 0:
            return 35
        elif numar % 3 == 0:
            return 3
        elif numar % 5 == 0:
            return 5
        else:
            return "Nediviibil_3_5"

    else:
        return "Nu este numar"


"""print(f"div_3_5 {div_3_5(15)} ")
print(f"div 3 {div_3_5(3)} ")
print(f"div 5 {div_3_5(5)}")
print(f"nedivizibil {div_3_5(7)}")
print(f"string {div_3_5("dsakkasdhjkass")}")
print(f" lista {div_3_5(["dada", 4, None])}")"""


