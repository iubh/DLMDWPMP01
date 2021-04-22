# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Iteratoren und Generatoren

#%%
# eine Liste mit der range()-Funktion generieren
my_range = list(range(0, 20, 3))

# den Iterator einer Liste aufrufen
my_iter = iter(my_range)

#%%
# den Iterator an die nächste Stelle schieben
next(my_iter)
# console output: 0

#%%
# eine Anweisung durchführen, die nicht direkt
# im Zusammenhang mit dem Iterator steht
print("nur ein Arm")

# den Iterator an die nächste Stelle schieben
next(my_iter)
# console output: 3

#%%
# den Iterator in einen StopIteration-Fehler laufen lassen
while True:
    next(my_iter)
# console output: StopIteration

#%%
# überprüfen, ob ein Objekt ein Iterator ist
dir(my_iter)
# included in the console output: __next__

#%%
hasattr(my_iter, "__next__")
# console output: True

#%%
hasattr(my_range, "__next__")
# console output: False

#%%
# eine Funktion definieren, die auf jedes Element einer
# Eingabeliste 1 addiert
def add_one(in_list):

    # eine leere Liste erzeugen
    out_list = []

    # über jedes Element in my_range iterieren
    for i in in_list:
        
        # auf das aktuelle Element 1 addieren
        i_plus_one = i + 1

        # das Ergebnis an die Ausgabeliste anhängen
        out_list.append(i_plus_one)

    # das Ergebnis ausgeben
    return(out_list)

#%%
# Funktion ausführen
add_one(my_range)
# console output: [1, 4, 7, 10, 13, 16, 19]

#%%
# eine Funktion definieren, die auf jedes Element einer
# Eingabeliste 1 addiert
def add_one_gen(in_list):

    # über jedes Element in my_range iterieren
    for i in in_list:
        
        # auf das aktuelle Element 1 addieren und dem
        # Generator übergeben
        yield i + 1

#%%
# Funktion ausführen
add_one_gen(my_range)
# console output: <generator object add_one_gen at 0x0000023582790970>

#%%
# über Generator iterieren
my_gen = add_one_gen(my_range)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# console output:
# 1
# 4
# 7

#%%
# Generator in eine Liste konvertieren
list(my_gen)
# console output: [10, 13, 16, 19]

#%%
# Generator in einen StopIterator-Fehler laufen lassen
my_gen = add_one_gen(my_range)
while True:
    next(my_gen)
# console output: StopIteration

#%%
# Generator mit List-Comprehension verwenden
my_gen = (i+1 for i in my_range)

# Generator anzeigen
print(my_gen)

# Generator in Liste konvertieren und anzeigen
print(list(my_gen))

#%%
# itertools-Modul laden
import itertools

# Iterator mit count()-Funktion erzeugen
my_iter = itertools.count(start=42, step=3)

# Testweise Elemente des Iterators ausgeben
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# console output:
# 42
# 45
# 48
# 51
# 54

#%%
# Iterator mit cycle()-Funktion
my_iter = itertools.cycle(["Brain", "Prian"])

# Testweise Elemente des Iterators ausgeben
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# console output:
# Brian
# Prian
# Brian
# Prian
# Brian

#%%
# Iterator mit cycle()-Funktion
my_iter = itertools.repeat("Romani ite domum", times=5)

# Testweise Elemente des Iterators ausgeben
list(my_iter)
# console output: 
# ['Romani ite domum',
#  'Romani ite domum',
#  'Romani ite domum',
#  'Romani ite domum',
#  'Romani ite domum']

