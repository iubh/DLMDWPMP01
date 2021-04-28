# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Unit- und Integrationstests

# in diesem Skript werden Funktionen definiert,
# die mit dem entsprechenden Test-Skript,
# 'my_functions_test.py' getestet werden

# Additionsfunktion definieren
def math_addition(number_1, number_2):
    '''
    Mathematische Addition
    number_1: Erste Zahl
    number_2: Zweite Zahl
    return: Addition der beiden Zahlen
    '''
    result = number_1 + number_2
    return result

# Divisionsfunktion definieren
def math_division(number_1, number_2):
    '''
    Mathematische Division
    number_1: Erste Zahl
    number_2: Zweite Zahl
    return: Subtraktion erste Zahl minus zweite Zahl
    '''
    
    # Division durch 0 abfangen
    if number_2 == 0:
        
        # in diesem Fall einen ValueError hervorrufen
        raise ValueError('you cannot divide by 0')
    
    result = number_1 / number_2
    return result