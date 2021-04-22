# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Schleifen

#%%
# eine Liste als Wertesammlung erzeugen
list_1 = [1, 7, 9, 23, 42]

# über jedes Element aus der Wertesammlung iterieren
for myItem in list_1:
    
    # das gerade betrachtete Element quadrieren
    print(myItem**2)

# console output:
# 1
# 49
# 81
# 529
# 1764

#%%
# Liste mit Vornamen aller Kollegen erzeugen
all_colleague = ['Jenny', 'Silke', 'Torben', 'Claudia', \
                 'Clemens', 'Dirk', 'Marta', 'Paul']

# leere Listen für beide Gruppen erzeugen
group_1 = []
group_2 = []

# iterativ alle Kollegen betrachten
for colleague in all_colleague:
    
    # beginnt der Vorname dieses Kollegen mit einem \
    # Buchstaben, der im Alphabet vor dem "M" steht?
    if colleague[0] < "M":
        
        # in diesem Fall wird dieser Kollege Gruppe 1 \
        # zugeteilt
        group_1.append(colleague)
    
    else:
        # andernfalls wird dieser Kollege Gruppe 2 \
        # zugeteilt
        group_2.append(colleague)

group_1
# console output: ['Jenny', 'Claudia', 'Clemens', 'Dirk']

group_2
# console output: ['Silke', 'Torben', 'Marta', 'Paul']

#%%
# eine Liste mit der range()-Funktion generieren
my_range = list(range(0, 20, 3))

# über die erzeugte Liste iterieren
for cur_item in my_range:
    print(cur_item)

# console output: 
# 0
# 3
# 6
# 9
# 12
# 15
# 18

#%%
for cur_item in my_range:
    
    # falls ein Wert größer sein sollte als 7
    # wird die Schleife vorzeitig beendet
    if cur_item > 7:
        break

    # den jeweiligen Wert in die Konsole ausgeben
    print(cur_item)

# console output: 
# 0
# 3
# 6

#%%
for cur_item in my_range:
    
    # falls ein Wert zwischen 5 und 14 liegt
    # wird "blank" in die Konsole geschrieben,
    # an den Anfang der Schleife gesprungen und
    # die Schleife erneut mit der nächsten Zählvariablen
    # durchlaufen
    if (cur_item > 5) & (cur_item < 14):
        print("blank")
        continue

    # den jeweiligen Wert in die Konsole ausgeben
    print(cur_item)


# console output: 
# 0
# 3
# blank
# blank
# blank
# 15
# 18

#%%
for cur_item in my_range:
    
    # falls ein Wert zwischen 5 und 14 liegt
    # wird nichts unternommen
    if (cur_item > 5) & (cur_item < 14):
        pass
    
    # in allen anderen Fällen wird der aktuelle
    # Wert der Zählvariablen ausgegeben
    else:
        print(cur_item)

# console output: 
# 0
# 3
# 15
# 18

#%%
x = 2

# verdoppele x bis x mindestens der Wert 1000 erreicht hat
while x < 1000:
    x *= 2

print(x)

# console output: 1024

