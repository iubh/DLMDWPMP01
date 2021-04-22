# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# diese Funktion ist zur Verwendung in einem anderen \
# Python-Skript gedacht

# Funktion definieren
def my_division(x, y):
    
    # Division durch 0 abfangen
    if y == 0:
        
        # in diesem Fall einen ValueError hervorrufen
        raise ValueError('you cannot divide by 0')

    # in allen anderen Fällen die Berechnung durchführen
    # und das Ergebnis zurückgeben
    output = x/y
    return(output)