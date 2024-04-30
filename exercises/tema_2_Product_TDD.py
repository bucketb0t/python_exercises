class ProductTDD:
    def __init__(self, product_name: str, product_price: float, product_discount: float, product_category: str):
        self.name = product_name
        self.price = product_price
        self.discount = product_discount
        self.category = product_category

    def final_price(self):
        return self.price - (self.price * self.discount)


# Create from CRUD
class ProductsManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self):
        return self.products

    def get_products_by_category(self, category):
        return [product.name for product in self.products if product.category == category]

    def get_products_with_final_price_under_a_value(self, value):
        return [product.name for product in self.products if product.final_price() < value]

    def get_product_names_by_discount(self, discount):
        return [product.name for product in self.products if product.discount == discount]

    """Tema Read, Update,Delete la manager"""

    def get_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        print("No product found")

    def update_product(self, n_Product, new_name, new_price, new_discount, new_category):
        retrieved_product = self.get_product_by_name(n_Product.name)
        if new_name:
            retrieved_product.name = new_name
            print(f"Old name {n_Product.name} updated to {retrieved_product.name}")
        if new_price:
            retrieved_product.price = new_price
            print(f"Old price {n_Product.price} updated to {retrieved_product.price}")
        if new_discount:
            retrieved_product.discount = new_discount
            print(f"Old discount {n_Product.discount} updated to {retrieved_product.discount}")
        if new_category:
            retrieved_product.category = new_category
            print(f"Old category {n_Product.category} updated to {retrieved_product.category}")

    # def update_product2(self, n_Product, new_name, new_price, new_discount, new_category):
    #     if n_Product in self.products:
    #         if new_name:
    #             n_Product.name = new_name
    #             print(f"Old name {n_Product.name} updated to {retrieved_product.name}")
    #         if new_price:
    #             n_Product.price = new_price
    #             print(f"Old price {n_Product.price} updated to {retrieved_product.price}")
    #         if new_discount:
    #             n_Product.discount = new_discount
    #             print(f"Old discount {n_Product.discount} updated to {retrieved_product.discount}")
    #         if new_category:
    #             n_Product.category = new_category
    #             print(f"Old category {n_Product.category} updated to {retrieved_product.category}")

    # def update_product(self, name, new_price, new_discount, new_category):
    #     # for product in self.products:
    #     #     if product.name == name:
    #     #         product.price = new_price
    #     #         product.discount = new_discount
    #     #         product.category = new_category
    #     #         return True
    #     return False  # Product not found

    def delete_product2(self, product_to_remove):
        lists_of_products = self.get_all_products()
        if product_to_remove not in lists_of_products:
            return f"Produsul {product_to_remove.name} nu se afla in lista"
        else:
            for product in lists_of_products:
                if product_to_remove == product:
                    lists_of_products.remove(product)
            return "Delete successful"

    def delete_product(self, product_to_remove):
        if product_to_remove in self.get_all_products():
            self.get_all_products().remove(product_to_remove)

# def delete_product(self, name):
#     for product in self.products:
#         if product.name == name:
#             self.products.remove(product)
#             return True
#


# Inițializarea obiectului de tip ProductsManager
products_manager = ProductsManager()

# Adăugarea de produse în ProductsManager folosind instanțe de ProductTDD
products_manager.add_product(ProductTDD("Paine", 10.0, 0.2, "Alimente"))
products_manager.add_product(ProductTDD("Bere", 15.0, 0.1, "Bauturi"))
products_manager.add_product(ProductTDD("Dero", 20.0, 0.15, "Menaj"))
products_manager.add_product(ProductTDD("Apa", 30.0, 0.25, "Alimente"))
products_manager.add_product(ProductTDD("Bere fara alcool", 25.0, 0.3, "Bauturi"))
products_manager.add_product(ProductTDD("Solutie curatat", 18.0, 0.12, "Menaj"))
products_manager.add_product(ProductTDD("Bere hipstareasca", 12.0, 0.05, "Bauturi"))
products_manager.add_product(ProductTDD("Iarasi Bere", 28.0, 0.2, "Bauturi"))
products_manager.add_product(ProductTDD("Apa", 22.0, 0.1, "Bauturi"))
products_manager.add_product(ProductTDD("Ciocolata", 17.0, 0.18, "Alimente"))
products_manager.add_product(ProductTDD("Suc", 19.0, 0.07, "Bauturi"))
products_manager.add_product(ProductTDD("Chipsuri", 21.0, 0.25, "Alimente"))
products_manager.add_product(ProductTDD("Jeleuri", 23.0, 0.3, "Alimente"))


