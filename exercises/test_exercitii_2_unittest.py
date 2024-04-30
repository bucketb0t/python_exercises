from exercitii_2 import div_3_5
import unittest


# PRIMUL MODUL DE TESTARE IN PYTHON

class TestReturnNumber(unittest.TestCase):
    def test_div_3_5_divizibil_cu_3_5(self):
        self.assertEqual(div_3_5(15), 35)

    def test_div_3_5_divizibil_cu_3(self):
        self.assertEqual(div_3_5(9), 3)

    def test_div_3_5_divizibil_cu_5(self):
        self.assertEqual(div_3_5(250), 5)
