# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# dieses Skript ist für unittests gedacht

# unittest-Modul und eigenes Skript laden
import unittest
import src_function

# eine Testklasse definieren, die die TestCases von
# unittest erbt
class TestSrcFunction(unittest.TestCase):

    # eine Testfunktion für my_division definieren
    def test_my_division(self):
        
        # einen exception-Test mit Kontext durchführen:
        # Wir erwarten einen ValueError, wenn wir
        # eine 0 als die Zahl übergeben, durch die
        # geteilt werden soll
        with self.assertRaises(ValueError):
            src_function.my_division(10, 0)

# dieses Skript im unittest-Kontext ausführen
if __name__ == '__main__':
    unittest.main()

# console output:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK
