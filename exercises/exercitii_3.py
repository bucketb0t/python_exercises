import self


class Product():
    def __init__(self, parametru_name: str = "No name", parametru_price: int = 0, parametru_discount: int = 0,
                 parametru_category: str = "No category"):

        self.category = parametru_category

        def switch_case(parametru_name):
            def convert_to_str(x):
                return str(x)

            def get_type(parametru_name):
                parametru_name_types = {"str": 1,
                                        "int": 2,
                                        "bool": 3,
                                        "float": 4,
                                        "list": 5,
                                        "None": 6}

                if isinstance(parametru_name, str):
                    return parametru_name_types.get("str")

                elif isinstance(parametru_name, int):
                    return parametru_name_types.get("int")

                elif isinstance(parametru_name, bool):
                    return parametru_name_types.get("bool")

                elif isinstance(parametru_name, float):
                    return parametru_name_types.get("float")

                elif isinstance(parametru_name, list):
                    return parametru_name_types.get("list")

                elif parametru_name is None:
                    return parametru_name_types.get("None")

                elif isinstance(parametru_name, dict):
                    raise Exception("Inputul e dictionar")

            match get_type(parametru_name):
                case 1:
                    return parametru_name
                case 2:
                    return convert_to_str(parametru_name)
                case 3:
                    return convert_to_str(parametru_name)
                case 4:
                    return convert_to_str(parametru_name)
                case 5:
                    # Varianta 1
                    p_str = ""
                    for p in parametru_name:
                        p_str += convert_to_str(p) + " "

                    # Varianta 2
                    p_str = ""

                    p_list = [convert_to_str(p) for p in parametru_name]
                    p_str = " ".join(p_list)

                    # Variant 3
                    p_str = " ".join([convert_to_str(p) for p in parametru_name])

                    return p_str

                case 6:
                    return convert_to_str(parametru_name)

        def elif_case(parametru_name):
            if isinstance(parametru_name, str):
                return parametru_name

            elif isinstance(parametru_name, int):
                return str(parametru_name)

            elif isinstance(parametru_name, bool):
                return str(parametru_name)

            elif isinstance(parametru_name, float):
                return str(parametru_name)

            elif isinstance(parametru_name, list):
                return " ".join([str(p) for p in parametru_name])

            elif parametru_name is None:
                return str(parametru_name)

            elif isinstance(parametru_name, dict):
                raise Exception("Inputul e dictionar")

        self.name = switch_case(parametru_name)
        # self.name=elif_case(parametru_name)

        """Acelasi model pentru cel facut impreuna, transformat fiecare in str"""
        self.price = parametru_price

        def switch_case(parametru_price):

            def switch_case(parametru_price):
                if isinstance(parametru_price, str):
                    return parametru_price

                elif isinstance(parametru_price, int):
                    return str(parametru_price)

                elif isinstance(parametru_price, bool):
                    return str(parametru_price)

                elif isinstance(parametru_price, float):
                    return str(parametru_price)

                elif isinstance(parametru_price, list):
                    return " ".join(map(str, parametru_price))

                elif parametru_price is None:
                    return str(parametru_price)

                elif isinstance(parametru_price, dict):
                    raise Exception("Inputul e dictionar")

            def elif_case(parametru_price):
                if isinstance(parametru_price, list):
                    return " ".join(map(str, parametru_price))

            return switch_case(parametru_price)

        self.discount = parametru_discount

        def switch_case(parametru_discount):

            if isinstance(parametru_discount, str):
                return parametru_discount

            elif isinstance(parametru_discount, int):
                return str(parametru_discount)

            elif isinstance(parametru_discount, bool):
                return str(parametru_discount)

            elif isinstance(parametru_discount, float):
                return str(parametru_discount)

            elif isinstance(parametru_discount, list):
                return " ".join(map(str, parametru_discount))

            elif parametru_discount is None:
                return str(parametru_discount)

            elif isinstance(parametru_discount, dict):
                raise Exception("Inputul e dictionar")

    def elif_case(parametru_discount):
        if isinstance(parametru_discount, list):
            return " ".join(map(str, parametru_discount))
        return switch_case(parametru_discount)

        # self.category = parametru_category

    def switch_case(parametru_category):
        if isinstance(parametru_category, str):
            return parametru_category

        elif isinstance(parametru_category, int):
            return str(parametru_category)

        elif isinstance(parametru_category, bool):
            return str(parametru_category)

        elif isinstance(parametru_category, float):
            return str(parametru_category)

        elif isinstance(parametru_category, list):
            return " ".join(map(str, parametru_category))

        elif parametru_category is None:
            return str(parametru_category)

        elif isinstance(parametru_category, dict):
            raise Exception("Inputul e dictionar")

    def elif_case(parametru_category):
        if isinstance(parametru_category, list):
            return " ".join(map(str, parametru_category))
        return switch_case(parametru_category)


def __str__(self):
    return f"Produs: {self.name}, Pret: {self.price}"


def __repr__(self):
    return str(self)


def __eq__(self, other):
    if not isinstance(other, Product):
        return False
    return self.name == other.name and self.price == other.price


def get_final_price(self):
    return self.price - self.price * self.discount / 100


# Adaugare de functii pentru setare si redenumire categorie si clasa, setare cost su discount
def get_category(self):
    return self.category


def set_category(self, new_category):
    self.category = new_category
    return self.category


def set_name(self, new_name):
    self.name = new_name
    return self.name


def get_name(self):
    return self.name


def get_discount(self):
    return self.discount


# Tema2
def set_discount(self, new_discount):
    self.discount = new_discount
    return new_discount


def get_price(self):
    return self.price


def set_price(self, new_price):
    self.price = new_price
    return new_price


p1 = Product(parametru_name="faina", parametru_price=100, parametru_discount=80, parametru_category="aliment de baza")

# print(p1.get_final_price())
# print(dir(p1))
# print(id(p1))
print(p1)

p2 = Product(parametru_name="faina", parametru_price=100, parametru_discount=0, parametru_category="bauturi")
print(p1 == p2)
if p1 == p2:
    print(f"P1 {p1.name} este identic cu P2 {p2.name}")
# y = Product(parametru_name="ClasaName")
# print(id(y.name), id(y.price))
'''
z = Product(parametru_name="ClasaFaraName")
# for z in dir(y):
#     print(z)

# De uitate peste __rep__ __init__ __str__ __eq__

print(y.name, z.name)'''

# In acelasi fisier
# Tema de facut pytest la get_final_price
# Prin metoda TDD sa se faca testare pt get_name, get_discount,get_price,get_category
# Prin metoda TDD sa se faca o metoda prin care sa se schimbe numele produsului si sa se numeasca functia set_name


# rularea testarilor
