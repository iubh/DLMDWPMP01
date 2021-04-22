# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Konditionaler Code

#%%
# Beispiel für erfüllte Bedingung
club = "Judäische Volksfront"

if club == "Judäische Volksfront":
    print("SPALTER")
# console output: SPALTER

#%%
# Beispiel für nicht erfüllte Bedingung
club = "Volksfront von Judäa"
if club == "Judäische Volksfront":
    print("SPALTER")
# no console output

#%%
# Ausgabe einer Ziffer, wenn diese in einem definierten
# Bereich liegt
my_digit = 3
if (my_digit > 10) & (my_digit < 18):
    print("hit it")
# no console output

#%%
my_digit = 16
if (my_digit > 10) & (my_digit < 18):
    print("hit it")
# console output: hit it

#%%
my_digit = 19
if (my_digit > 10) & (my_digit < 18):
    print("hit it")
# no console output

#%%
# ist eine Zahl restlos durch 2 teilbar?
my_number = 23
if my_number % 2 == 0:
    print("gerade")
else:
    print("ungerade")
# console output: ungerade

#%%
# Evaluation mehrerer Bedingungen
location = "Berlin"
if location == "Freiburg":
    print("Seele")
elif location == "Berlin":
    print("Schrippe")
else:
    print("Brötchen")
# console output: Schrippe
