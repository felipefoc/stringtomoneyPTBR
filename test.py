import unittest
from functions import _milhao, _milhar, _reais
from validator import validate_line
from classes import Cents


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.cents1 = Cents("84").cents_extense()
        self.cents2 = Cents("10").cents_extense()
        self.cents3 = Cents("11").cents_extense()

    def test_reais(self):
        self.assertEqual(_reais(123), "cento e vinte e três reais")
        self.assertEqual(_reais(999), "novecentos e noventa e nove reais")
        self.assertEqual(_reais(25), "vinte e cinco reais")

    def test_milhar(self):
        self.assertEqual(
            _milhar(123456),
            "cento e vinte e três mil quatrocentos e cinquenta e seis reais",
        )
        self.assertEqual(
            _milhar(999999),
            "novecentos e noventa e nove mil novecentos e noventa e nove reais",
        )
        self.assertEqual(_milhar(107102), "cento e sete mil cento e dois reais")

    def test_milhao(self):
        self.assertEqual(
            _milhao(123456789),
            "cento e vinte três milhões e quatrocentos e cinquenta e seis mil e setecentos e oitenta e nove reais",
        )
        self.assertEqual(
            _milhao(102104222),
            "cento e dois milhões e cento e quatro mil e duzentos e vinte e dois reais",
        )
        self.assertEqual(
            _milhao(1222987),
            "um milhão e duzentos e vinte e dois mil e novecentos e oitenta e sete reais",
        )

    def test_cents(self):
        self.assertEqual(self.cents1, "e oitenta e quatro centavos")
        self.assertEqual(self.cents2, "e dez centavos")
        self.assertEqual(self.cents3, "e onze centavos")

    def test_validation(self):
        self.assertTrue(validate_line("123456,00"))
        self.assertTrue(validate_line("00121,00"))
        self.assertFalse(validate_line(65465))
        self.assertFalse(validate_line("6556,0"))


if __name__ == "__main__":
    unittest.main()
