# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Dokumentation des Codes

## Block-Kommentare

# dieser Code führt folgende mathematischen Operationen durch
# Addition
# Subtraktion
# Division

## Inline-Kommentare

# der folgende Code führt verschiedene mathematische Operationen durch
add_1 = 4 + 3   # Addition
sub_1 = 4 - 3   # Subtraktion
div_1 = 4 / 3   # Division

## Docstring-Kommentare

def math_addition(self, number_1, number_2):
         '''
         mathematische Addition 
         number_1: erste Zahl
         number_2: zweite Zahl
         return: Addition der beiden Zahlen
         '''
         result = number_1 + number_2
         return result

