#Tema 1

# Clase cu atribute diferite
class ClasaA:
    def __init__(self, a):
        self.a = a

class ClasaB:
    def __init__(self, b):
        self.b = b

class ClasaC(ClasaA, ClasaB):
    def __init__(self,a,b, c):
        ClasaA.__init__(self, a)
        ClasaB.__init__(self, b)
        #How to do super inheritance
        self.c = c

    def calcule(self):
        # Calcul între atributele claselor respective
        result = self.a * self.b * self.c
        return result

# Exemplu de utilizare
obj_C = ClasaC(2, 3, 4)
print(obj_C.calcule())  # Va afișa rezultatul calculului: 24 (2 * 3 * 4)


#test Tema 1

def test_calcule():
    obj_C = ClasaC(2,3,4)
    assert obj_C.calcule() == 24