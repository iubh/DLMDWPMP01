# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Beschleunigung von Python

#%%
# Packages laden
from numba import jit
import time
from time import process_time
import numpy as np

# Rechenintensive Funktion definieren
def sum2dimensional(np_array):
    array_rows, array_columns = np_array.shape
    result = 0.0
    for i in range(array_rows):
        for j in range(array_columns):
            result += np_array[i,j]
    return result

#%%
# Startzeit der Berechnung aufzeichnen
start_time = process_time() 

# Berechnung durchführen
np_array = np.arange(100000000).reshape(10000, 10000)

# Ergebnis der Berechnung ausgeben
print(sum2dimensional(np_array))

#%%
# Endzeit der Berechnung aufzeichnen
end_time = process_time() 

# Differenz aus Start- und Endzeit berechnen
print(end_time - start_time)
# console output: 25.046875

#%%
# Dekorator verwenden, um anzugeben, ob der Code
# als Maschinencode kompiliert werden soll
@jit(nopython=True)
def sum2dimensional(np_array):
    array_rows, array_columns = np_array.shape
    result = 0.0
    for i in range(array_rows):
        for j in range(array_columns):
            result += np_array[i,j]
    return result

#%%
start_time = process_time() 
np_array = np.arange(100000000).reshape(10000, 10000)
print(sum2dimensional(np_array))
end_time = process_time() 
print(end_time - start_time)

# console output: 0.3125

