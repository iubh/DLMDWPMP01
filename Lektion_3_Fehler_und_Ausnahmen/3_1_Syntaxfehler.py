# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Syntaxfehler

#%%
# eine überflüssige Klammer am Ende der Zeile
print(1/1))

# console output:
# File "<ipython-input-2-be2387ae642c>", line 2
#    print(1/1))
#              ^
# SyntaxError: unmatched ')'

#%%
# Division durch 0
print(1/0)

# cosole output:
# ----> 19 print(1/0)
# ZeroDivisionError: division by zero

#%%
# logischer Fehler
brian = 'naughty boy'
print(prian)

# console output:
# ----> 28 print(prian)
# NameError: name 'prian' is not defined

#%%
# sys-package laden und aktuelle exceptions zeigen
import sys
sys.exc_info()
# console ouput: (None, None, None)

# Exception erzeugen und Info anzeigen

# versuche folgenden Code auszuführen
try:
    1/0

# führe folgenden Code bei einem ZeroDivisionError aus
except ZeroDivisionError:
    print(sys.exc_info())

# console output:
# (<class 'ZeroDivisionError'>,
# ZeroDivisionError('division by zero'),
# <traceback object at 0x0000024D33EAFC40>)

