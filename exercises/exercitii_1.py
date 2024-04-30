x = 2
print(id(x))

print(id(2))
y = x
z = y
print(id(y))
x = 3
print(id(x))
print(id(y))
print(id(3))

lista = ["a", 2, 4, True, None]
print(len(lista))
lista2 = ["ioi", 7, 7436743673, lista]
print(len(lista2))
print(len("ioi"))
lista.append("ytewtyew")
print(lista)
print(lista.pop(1))
print(lista.remove("a"))
print(lista)
# Comment
'''dalihdsalhdsaljhdsajsdahkfhajkgfajkgfajkgdkjagdkjadg
fkjaljksajlk
jsfjlakjlkadas'''

a = {"key1": "454",
     3: "454"
     }
print(a)
a[3] = 5
print(f"tejerjjhaa {a} \\ asjdashdasj")
b = {3: "500",
     True: 3}
print(b)
a.update(b)
print(a)
