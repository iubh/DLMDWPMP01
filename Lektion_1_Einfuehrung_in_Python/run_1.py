# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

#%%
# Funktion aus einem anderen Python-Skript importieren
import src_1

# Funktion ausführen
src_1.what_a_function(9, 42)

#%%
# Funktion aus einem Skript in einem Unterordner importieren
import source_scripts.src_1

# Funktion ausführen
source_scripts.src_1.what_a_function(9, 42)

#%%
# eine bestimmte Funktion aus einem Skript importieren
from source_scripts.src_1 import what_a_function

# Funktion ausführen
what_a_function(9, 42)