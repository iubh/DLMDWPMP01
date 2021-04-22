# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Module und Pakete

#%%
# eine Funktion aus einem Modul laden
from os import getcwd

# Funktion im Programm verwenden
getcwd()

#%%
# das gesamt Modul laden
import os

# eine Funktion aus dem Modul verwenden
os.path.isfile("myTextData.txt")
# console output: True

#%%
# das Modul unter anderem Namen laden
import os as o

# diesen Namen im Programm verwenden
o.path.isfile("myTextData.txt")
# console output: True