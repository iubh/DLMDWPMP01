# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Eingabe / Ausgabe

#%%
# Eine Tastatur-Eingabe abfragen
user_input = input("Wie heißt du?")

#%%
# Die Eingabe ausgeben
print("Hallo, {}!".format(user_input))
# console output: Hallo, Christian!

#%%
# Datei im Lese-Modus öffnen
my_file = open("myTextData.txt", "r")

# Inhalt der Datei lesen und als Objekt speichern
my_file_content = my_file.read()

# Datei schließen
my_file.close()

# in Objekt gespeicherten Inhalt ausgeben lassen
print(my_file_content)
# console output: 
# Strange women lying in ponds,
# distributing swords,
# is no basis for a
# system of government!

#%%
# Datei sicher öffnen
with open("myTextData.txt", "r") as my_file:
    
    # Inhalt der Datei lesen und als Objekt speichern
    my_file_content = my_file.read()

#%%
with open("myTextData.txt", "r") as my_file:
    
    # über jede Zeile der Datei iterieren
    for cur_line in my_file:
        print("This line: {}".format(cur_line))
# console output: 
# This line: Strange women lying in ponds,
# This line: distributing swords,
# This line: is no basis for a
# This line: system of government!


#%%
with open("myTextData.txt", "r") as my_file:
    my_line = my_file.readline()
print(my_line)
# console output: Strange women lying in ponds,

#%%
with open("myTextData.txt", "r") as my_file:
    my_lines = my_file.readlines()
print(my_lines[3])
# console output: system of government!

#%%
with open("myNewTextData.txt", "w") as my_file:
    my_file.write("blessed are the cheesemakers.")