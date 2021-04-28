# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Unit- und Integrationstests

'''
Dieses Skript führt unittests für die in
'my_functions.py' definierten Funktionen
durch
'''

# unittest-Modul und zu testendes Skript laden
import unittest
import my_functions as mf

# eine Testklasse definieren, die die TestCases von
# unittest erbt
class UnitTestMathOperations(unittest.TestCase):

    # eine Testfunktion für math_addition definieren
    def test_math_addition(self):
        '''
        Mathematische Addition testen
        '''
        result = mf.math_addition(2, 2)
        self.assertEqual(result, 4, "Die Addition sollte 4 ergeben")

    # eine Testfunktion für math_division definieren
    def test_math_division(self):
        '''
        Mathematische Division testen
        '''
        
        # einfache Division
        result = mf.math_division(6, 2)
        self.assertEqual(result, 3, "Die Division sollte 3 ergeben")

        # einen exception-Test mit Kontext durchführen:
        # Wir erwarten einen ValueError, wenn wir
        # eine 0 als die Zahl übergeben, durch die
        # geteilt werden soll
        with self.assertRaises(ValueError):
            mf.math_division(10, 0)

# dieses Skript im unittest-Kontext ausführen
if __name__ == '__main__':
    unittest.main()