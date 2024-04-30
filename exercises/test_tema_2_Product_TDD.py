import pytest
from tema_2_Product_TDD import ProductTDD, ProductsManager


class TestTema2:

    def setup_method(self):
        self.products_manager = ProductsManager()
        self.products_manager.add_product(ProductTDD("Paine", 10.0, 0.2, "Alimente"))
        self.products_manager.add_product(ProductTDD("Bere", 15.0, 0.1, "Bauturi"))
        self.products_manager.add_product(ProductTDD("Dero", 20.0, 0.15, "Menaj"))
        self.products_manager.add_product(ProductTDD("Apa", 30.0, 0.25, "Alimente"))
        self.products_manager.add_product(ProductTDD("Bere fara alcool", 25.0, 0.3, "Bauturi"))
        self.products_manager.add_product(ProductTDD("Solutie curatat", 18.0, 0.12, "Menaj"))
        self.products_manager.add_product(ProductTDD("Bere hipstareasca", 12.0, 0.05, "Bauturi"))
        self.products_manager.add_product(ProductTDD("Iarasi Bere", 28.0, 0.2, "Bauturi"))
        self.products_manager.add_product(ProductTDD("Apa", 22.0, 0.1, "Bauturi"))
        self.products_manager.add_product(ProductTDD("Ciocolata", 17.0, 0.18, "Alimente"))
        self.products_manager.add_product(ProductTDD("Suc", 19.0, 0.07, "Bauturi"))
        self.products_manager.add_product(ProductTDD("Chipsuri", 21.0, 0.25, "Alimente"))
        self.products_manager.add_product(ProductTDD("Jeleuri", 23.0, 0.3, "Alimente"))

        """ CRUD TESTING"""

        self.products_manager2 = ProductsManager()

        # @pytest.fixture

    # def initialized_product_tdd():
    #     products_manager = ProductsManager()
    #     products_manager.add_product(ProductTDD("Paine", 10.0, 0.2, "Alimente"))
    #     return products_manager

    # Testarea prețurilor finale pentru produse
    # @pytest.mark.parametrize("input_data, expected_output", [
    #     (["Paine", "Bere"], 2),
    #     (["Paine"], 1),
    #     ([], 0),
    # ])
    # def test_get_all_products(self, input_data, expected_output):
    #     #product_tdd = initialized_product_tdd
    #     for product_name in input_data:
    #         self.products_manager.add_product(ProductTDD(product_name, 10.0, 0.1, "Test"))
    #     assert len(self.products_manager.get_all_products()) == expected_output

    def test_get_all_products(self):
        print(self.products_manager.products)
        assert self.products_manager.get_all_products() == self.products_manager.products

    # Obținerea numelui produselor în funcție de discount.
    # @pytest.mark.parametrize("product_name, expected_output", [
    #     ("Paine", "Paine"),
    #     ("Bere", "Bere"),
    #     ("Nonexistent", None),
    # ])
    # def test_get_product_by_name(self, product_name, expected_output):
    #     #product_tdd = initialized_product_tdd
    #     result = self.products_manager.get_product_by_name(product_name)
    #     assert (result.name if result else result) == expected_output

    @pytest.mark.parametrize("product_name, expected_output", [
        ("Bere hipstareasca", ProductTDD("Bere hipstareasca", 12.0, 0.05, "Bauturi"))
    ])
    def test_get_product_by_name(self, product_name, expected_output):
        assert self.products_manager.get_product_by_name(product_name) == expected_output

    # Manipularea produselor în funcție de valori extreme pentru discounturi
    @pytest.mark.parametrize("category, expected_output", [
        ("Bauturi", ["Bere"]),
        ("Alimente", ["Paine"]),
        ("Test", []),
    ])
    def test_get_products_by_category(self, category, expected_output):
        # product_tdd = initialized_product_tdd
        result = self.products_manager.get_products_by_category(category)
        assert [product.name for product in result] == expected_output

    # Testarea prețurilor finale pentru produse sub o anumită valoare:
    @pytest.mark.parametrize("input_data, expected_output", [
        (None, []),  # Caz input None
        (-1, []),  # Caz input cu valoare negativă
        (15, ['Paine', 'Bere']),  # Caz funcționare normală (preț sub 15)
    ])
    def test_get_products_with_final_price_under_a_value(self, input_data, expected_output):
        # product_tdd = initialized_product_tdd
        result = self.products_manager.get_products_with_final_price_under_a_value(input_data)
        assert result == expected_output

    # Obținerea numelui produselor în funcție de discount:
    @pytest.mark.parametrize("input_data, expected_output", [
        (None, []),  # Caz input None
        (-0.1, []),  # Caz input cu discount negativ
        (0.2, ['Paine', 'Bere']),  # Caz funcționare normală (produse cu discount de 20%)
    ])
    def test_get_product_names_by_discount(self, input_data, expected_output):
        # product_tdd = initialized_product_tdd
        result = self.products_manager.get_product_names_by_discount(input_data)
        assert result == expected_output

    # Create

    @pytest.mark.parametrize("input_data, expected_output", [(ProductTDD("Bere hipstareasca", 12.0, 0.05, "Bauturi"),
                                                              1),
                                                             (ProductTDD("Jeleuri", 23.0, 0.3, "Alimente"),
                                                              1)
                                                             ])
    def test_add_product(self, input_data, expected_output):
        print(len(self.products_manager2.products))
        self.products_manager2.add_product(input_data)
        result = self.products_manager2.get_all_products()
        assert len(result) == expected_output
        assert id(result[-1]) == id(input_data)

    # De facut read
    @pytest.mark.parametrize("input_data", [
        (ProductTDD("Bere hipstareasca", 12.0, 0.05, "Bauturi"))
        ])
    def test_get_all_products(self, input_data):
        self.products_manager2.add_product(input_data)
        result = self.products_manager2.get_all_products()
        assert result == [input_data]

        # Update

    @pytest.mark.parametrize("input_data1, input_data2,input_data3,input_data4,input_data5", [
        (ProductTDD("Bere hipstareasca", 12.0, 0.05, "Bauturi"), "hipstareasca bere", 31, 80, "painea lichida")
    ])
    def test_update_product(self, input_data1, input_data2, input_data3, input_data4, input_data5):
        self.products_manager2.add_product(input_data1)
        self.products_manager2.update_product(input_data1, input_data2, input_data3, input_data4, input_data5)
        result = self.products_manager2.get_product_by_name(input_data2)
        assert result.name == input_data2
        assert result.price == input_data3
        assert result.discount == input_data4
        assert result.category == input_data5
        assert id(result) == id(input_data1)

    # De facut delete

    @pytest.mark.parametrize("input_data, expected_output", [
        (ProductTDD("Bere hipstareasca", 12.0, 0.05, "Bauturi"), 0),
    ])
    def test_delete_product(self, input_data, expected_output):
        self.products_manager2.add_product(input_data)
        successful_delete = self.products_manager2.delete_product2(input_data)
        result2 = self.products_manager2.get_all_products()

        # Assert pentru verificare successful delete
        assert len(result2) == expected_output
        assert result2 == []
        assert successful_delete == "Delete successful"

        # Block-ul se ocupa de verificare fail delete
        successful_delete = self.products_manager2.delete_product2(input_data)
        assert successful_delete == f"Produsul {input_data.name} nu se afla in lista"
