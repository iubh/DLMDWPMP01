# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Datenstrukturen

#%%
# Fließkomma-Variable definieren
pi = 3.14

# Ganzzahl-Variable definieren
x = 1

# Datentyp abfragen 
type(x)
# console output: int

# auf eine Ganzzahl-Variable eine Fließkomma-Variable addieren 
x += pi

# Datentyp abfragen 
type(x)
# console output: float

#%%
# eine Integer-Variable erzeugen und abfragen
year = 2019
isinstance(year, int)
# console output: True

#%%
# eine Float-Variable erzeugen und abfragen
pi = 3.14
isinstance(pi, float)
# console output: True
        
#%%
# eine String-Variable erzeugen und abfragen
mustbefirst = "Hello World!"
isinstance(mustbefirst, str)
# console output: True

#%%
# Abfragen nach Datenstruktur machen
int_test_1 = isinstance(year, int)
# console output: True

int_test_2 = isinstance(pi, int)
# console output: False

int_test_3 = isinstance(mustbefirst, int)
# console output: False

# überprüfen, welche Datenstruktur die Funktion isinstace() zurückgibt 
type(int_test_1)
# console output: bool

# wie viele Variablen sind Integer-Variablen?
sum([isinstance(year, int), \
     isinstance(pi, int), \
     isinstance(mustbefirst, int)])
# console output: 1

#%%
# einen String erzeugen
string_1 = "Judäische Volksfront?! Quatsch!"

# einzelne Zeichen eines Strings ansprechen
string_1[1]
# console output: 'u'

#%%
# einen Slice ausgeben
string_1[10:22]
# console output: 'Volksfront?!'

#%%
# einen Slice bis zum Ende des Strings ausgeben
string_1[10:]
# console output: 'Volksfront?! Quatsch!'

#%%
# die letzten 7 Zeichen anzeigen lassen
string_1[-8:]
# console output: 'Quatsch!'

#%%
# die ersten n Zeichen eines Strings ausgeben lassen
string_1[:9]
# console output: 'Judäische'

#%%
# alles anzeigen, außer die letzten 8 Zeichen
string_1[:-9]
# console output: 'Judäische Volksfront?!'

#%%
# Versuch, ein Element eines Strings zu überschreiben
string_1[1] = "ooo"
# Fehler: 'str' object does not support item assignment

#%%
# ID des String-Objektes abfragen
id(string_1)
# console output: 1982687046320

string_1 += " Wir sind die Volksfront von Judäha!"
string_1
# console output: 'Judäische Volksfront?! Quatsch! \
#                  Wir sind die Volksfront von Judäha!'

# ID des String-Objektes abfragen
id(string_1)
# console output: 1982687095520

#%%
# join()-Funktion für eine String-Verkettung nutzen
string_2 = " - ".join([string_1, "SPALTER!!!"])
string_2
# console output: 'Judäische Volksfront?! Quatsch! \
#                  Wir sind die Volksfront von \
#                  Judäha! - SPALTER!!!'

#%%
# Länge eines Strings ausgeben lassen
len(string_1)
# console output: 79

#%%
# Elemente zählen
string_1.count("ä")
# console output: 2

#%%
# überprüfen, ob eine Zeichenfolge in einem String \
# enthalten ist
"Quatsch" in string_1
# console output: True

# überprüfen, ob eine Zeichenfolge in einem String \
# nicht enthalten ist
"Messias" not in string_1
# console output: True

#%%
# einen Substring in einem String finden
string_2.find("SPALTER")
# console output: 70

#%%
# find()-Funktion als Hilfsfunktion beim Slicing
string_2[string_2.find("SPALTER"):]
# console output: 'SPALTER!!!'

#%%
# die find()-Funktion ist case-sensitive
string_2.find("spalter")
# console output: -1
# bedeutet: ist nicht vorhanden

#%%
# einen String in Großbuchstaben überführen
"spalter".upper()
# console output: 'SPALTER'

#%%
# die upper()-Funktion kann für case-insentivive \
# Abfragen genutzt werden
string_2.find("spalter".upper())
# console output: 70

#%%
# alle Großbuchstaben in Kleinbuchstaben konvertieren
string_2.lower()
# console output: 'judäische volksfront?! quatsch! \
# wir sind die volksfront von judäha! - spalter!!!'

#%%
# Zeichen innerhalb des Strings austauschen
string_1.replace("ä", "ae")
# console output: 'Judaeische Volksfront?! Quatsch! \
#                  Wir sind die Volksfront von Judaeha!'

#%%
# einen String in mehere Elemente aufspalten
string_1.split("!")
# console output: ['Judäische Volksfront?', \
#                  ' Quatsch', \
#                  ' Wir sind die Volksfront von Judäha', \
#                  '']

#%%
# Leerzeichen am Anfang und Ende eines Strings entfernen
" Quatsch".strip()
# console output: 'Quatsch'

#%%
# einen String explizit mit der print()-Funktion ausgeben
print(string_1)
# console output: Judäische Volksfront?! Quatsch! Wir \
# sind die Volksfront von Judäha!

#%%
# einen String dynamisch generieren 
print("1. Zeichen: {}, 2. Zeichen: {}".format(string_1[0], \
                                              string_1[1]))
# console output: 1. Zeichen: J, 2. Zeichen: u

#%%
# einen String mit Zeilenumbruch dynamisch generieren 
print("1. Zeichen: {}, \n2. Zeichen: {}".format(string_1[0], \
                                                string_1[1]))
# console output: 1. Zeichen: J, \
#                 2. Zeichen: u

#%%
# eine Liste generieren
list_1 = ["Torben", "Silke", "Bernd"]

#%%
# ein Element mit Indexing abrufen
list_1[0]
# console output: 'Torben'

#%%
# Elemente aus der Liste mit Slicing abrufen
# hier fragen wir nach allen Elementen
# von Index 1 bis zum Ende der List
list_1[1:]
# console output: ['Silke', 'Bernd']

#%%
# eine sortierte Liste erzeugen
list_2 = sorted(list_1)
list_2
# console output: ['Bernd', 'Silke', 'Torben']

#%%
# die Identifikationsnummer der Objekte erfragen
id(list_1)
# console output: 1630637091904
id(list_2)
# console output: 1630636857408

#%%
# die Liste Inplace sortieren
list_1.sort()
list_1
# console output: ['Bernd', 'Silke', 'Torben']

#%%
# Reihenfolge in list_2 (alphabetisch sortiert) umdrehen
list_2.reverse()
list_2
# console output: ['Torben', 'Silke', 'Bernd']

#%%
# den Index eines Elementes erfragen
list_1.index("Torben")
# console output: 2

#%%
# ein Element an eine bestehende Liste anhängen
list_1.append("Claudia")
list_1
# console output: ['Bernd', 'Silke', 'Torben', 'Claudia']

#%%
# ein Element der Liste überschreiben
list_1[0] = "Jenny"
list_1
# console output: ['Jenny', 'Silke', 'Torben', 'Claudia']

#%%
# Unpacking
homie_1, homie_2, homie_3, homie_4 = list_1
homie_2
# console output: 'Silke'

#%%
# ein Element aus einer Liste löschen
del(list_1[3])
list_1
# console output: ['Jenny', 'Silke', 'Torben']

#%%
# primitive Datenstrukturen als Elemente
# einer Liste mischen
list_3 = [1, 2, 3, "a", "b", "c", True, False]
# es tritt kein Fehler auf


# %%
# zwei Listen kombinieren (+-Notation)
comb_list_1 = list_1 + list_3
comb_list_1
# console output: ['Jenny', 'Silke', 'Torben', 1, 2, 3, \
# 'a', 'b', 'c', True, False]

# zwei Listen kombinieren (extend()-Funktion)
list_1.extend(list_3)
list_1
# console output: ['Jenny', 'Silke', 'Torben', 1, 2, 3, \
# 'a', 'b', # 'c', True, False]

#%%
# wie viele Elemente hat eine Liste?
len(list_1)
# console output: 11

#%%
# eine Liste in eine Liste integrieren
list_2.insert(1, list_3)
list_2
# console output: ['Torben', \
# [1, 2, 3, 'a', 'b', 'c', True, False], \
# 'Silke', 'Bernd']

#%%
# Abfrage nach dem Enthaltensein eines Elementes \
# in einer Liste
"Silke" in list_1
# console output: True

# Abfrage nach dem Nicht-Enthaltensein eines Elementes \
# in einer Liste
"Dieter" not in list_1
# console output: True

#%%
# einen Tupel erzeugen
tuple_1 = ("Torben", "Silke", "Bernd")

#%%
# ein Element aus einem Tupel abfragen
tuple_1[1]
# console output: 'Silke'

# Versuch, ein Element des Tupels zu verändern
tuple_1[1] = "Claudia"
# Fehler: 'tuple' object does not support item assignment

#%%
# Versuch, eine Element an einen Tupel anzufügen
tuple_1.extend("Claudia")
# Fehler: 'tuple' object has no attribute 'extend'

#%%
# einen zweiten Tupel erzeugen
tuple_2 = ("Claudia", "Jens")

# id von tuple_1 ausgeben lassen
id(tuple_1)
# console output: 2127994382528

# Tupel verketten
tuple_1 += tuple_2
tuple_1
# console output: ('Torben', 'Silke', 'Bernd', \
#                  'Claudia', 'Jens')

# id von tuple_1 ausgeben lassen
id(tuple_1)
# console output: 2127991125936

#%%
# eine Liste in einem Tupel erzeugen
tuple_3 = ("Torben", ["Python, R"], \
           "Claudia", ["Python", "Java"])

# ein Element in einer Liste innerhalb \
# eines Tupels ändern
tuple_3[3][1] = "C#"
tuple_3
# console output: ('Torben', ['Python, R'], \
#                  'Claudia', ['Python', 'C#'])

#%%
# ein Set erzeugen
set_1 = {"Schraube", "Mutter", "Schraube", \
         "Nagel", "Mutter", "Dübel"}
set_1
# console output: {'Dübel', 'Mutter', 'Nagel', 'Schraube'}

#%%
# Versuch, ein Element eines Sets zu ändern
set_1[2] = "Nagel"
# Fehler: 'set' object is not subscriptable

#%%
# ein Set um ein Element erweitern
set_1.add("Winkel")
set_1
# console output: {'Dübel', 'Mutter', 'Nagel', \
#                  'Schraube', 'Winkel'}

#%%
# ein zweites Set erzeugen
set_2 = {'Haken', 'Winkel', 'Steg', \
         'Pinökel', 'Schraube'}

# mathematische Schnittmenge abfragen
set_1 & set_2
# console output: {'Schraube', 'Winkel'}

#%%
# ein Frozenset erzeugen
frozenset_1 = frozenset(list_3)
frozenset_1
# console output: frozenset({1, 2, 3, False, 'a', 'b', 'c'})

# Versuch, ein Element eines Frozensets zu verändern
frozenset_1[1] = 'Jon'
# Fehler: 'frozenset' object does not support item assignment

# Versuch, ein Element an ein Frozenset anzuhängen
frozenset_1.add('Klaus')
# Fehler: 'frozenset' object does not support item assignment

#%%
# ein Dictionary erzeugen
dict_1 = {"Montag": 24.3, "Dienstag": 25.7, "Mittwoch": 28.9}

#%%
# ID des Dictionaries abfragen
id(dict_1)
# console output: 2438680281472

# ein Element überschreiben
dict_1["Dienstag"] = 31.2
dict_1
# console output:
{'Montag': 24.3, 'Dienstag': 31.2, 'Mittwoch': 28.9}

# ID des Dictionaries abfragen
id(dict_1)
# console output: 2438680281472

#%%
# ist ein Element im Dictionary enthalten?
"Montag" in dict_1
# console output: True

#%%
# Werte (values) eines Dictionaries anzeigen
dict_1.values()
# console output: dict_values([24.3, 31.2, 28.9])

# ist ein Wert (value) in einem Dictionary enthalten?
31.2 in dict_1.values()
# console output: True

#%%
# Schlüssel (keys) eines Dictionaries anzeigen
dict_1.keys()
# console output: dict_keys(['Montag', 'Dienstag', 'Mittwoch'])

# Schlüssel-Werte-Paare anzeigen lassen
dict_1.items()
# console output: dict_items([('Montag', 24.3), \
#                             ('Dienstag', 31.2), \
#                             ('Mittwoch', 28.9)])
