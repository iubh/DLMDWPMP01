# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Funktionen

#%%
# eine Funktion definieren
def what_a_function(x, y):
    """
    This function sums up its two inputs and
    returns the quadratic of this sum

    input arguments:
    - x: numeric
    - y: numeric 

    dependencies:
    - none

    output arguments:
    The quadratic of the sum of inputs
    """
    
    # add the two input arguments
    z = x + y

    # square this sum
    out = z**2

    # return the results from the function
    return(out)

#%%
# die Funktion mit Argumenten aufrufen
what_a_function(2, 7)
# console output: 81

#%%
# die Funktion mit anderen Argumenten aufrufen
what_a_function(9, 42)
# console output: 2601

#%%
# eine Funktion mit Standardparametern definieren
def what_a_function(x, y=42):
    z = x + y
    out = z**2
    return(out)

#%%
# Die Funktion mit Standardparameter ausführen
what_a_function(x=3)
# console output: 2025

#%%
# Standardparameter der Funktion überschreiben
what_a_function(x=3, y=7)
# console output: 100

#%%
# eine Funktion mit unbestimmter Anzahl von Funktions-
# argumenten definieren
def some_of_unknowns(*args):
    out = sum(args)
    print(out)

#%%
# Funktion mit zwei Funktionsargumenten aufrufen
some_of_unknowns(9, 42)
# console output: 51

# Funktion mit 5 Funktionsargumenten aufrufen
some_of_unknowns(7, 3, 6)
# console output: 16

# Funktion mit einem Funktionsargument aufrufen
some_of_unknowns(42)
# console output: 42

# Funktion mit 0 Funktionsargumenten aufrufen
some_of_unknowns()
# console output: 0

#%%
# eine Funktion mit unbestimmter Anzahl von Elementen
# im dictionary-Stil definieren
def some_of_unknowns(**args):
    out = sum(args.values())
    return(out)

#%%
# Funktion mit 3 Funktionsargumenten ausführen
some_of_unknowns(first=3, second=7, third=9)
# console output: 19

# Funktion mit 5 Funktionsargumenten ausführen
some_of_unknowns(first=3, second=7, third=9, \
                 fourth=42, fifth=23)
# console output: 84

#%%
# Funktion mit lokalen Variablen definieren
def what_a_function(x=3, y=42):
    z_local = x + y
    out = z_local**2
    return(out)

# lokale Variable im übergeordneten Scope aufrufen
print(z_local)
# console output: NameError: name 'z' is not defined

#%%
# lokalen Variablen an die ausführende Instanz übergeben
def what_a_function(x=3, y=42):
    global z_global
    z_global = x + y
    out = z_global**2
    return(out)

# lokale Variable im übergeordneten Scope aufrufen
what_a_function()
print(z_global)
# console output: 45

#%%
# eine globale Variable erzeugen
todaysDay = 5

# eine Funktion definieren, die den Tag
# in n Wochen berechnet
def n_weeks_later(n_weeks):
    
    # implizit auf eine globale Variable (todaysDay) verweisen
    out = todaysDay + (n_weeks * 7)
    return(out)

# Funktion ausführen
n_weeks_later(5)
# console output: 40

#%%
# eine globale Variable erzeugen
todaysDay_global = 5

# eine Funktion definieren, die den Tag
# in n Wochen berechnet
def n_weeks_later(n_weeks, todaysDay_local=5):
    
    out = todaysDay_local + (n_weeks * 7)
    return(out)

# Funktion ausführen
n_weeks_later(5, todaysDay_local=todaysDay_global)
# console output: 40

#%%
# äußere Funktion definieren
def outer_func():
    
    # eine lokale im Scope outer_func definieren
    x = "Judäische Volksfront"

    # inner Funktion definieren
    def inner_func():
        
        # Versuch die Variable in übergeordneten
        # Scope zu überschreiben
        x = "Volksfront von Judäa"
    
    # innere Funktion innerhalb der äußeren Funktion aufrufen
    inner_func()
    
    return(x)

# äußere und darin enthaltene innere Funktion ausführen
outer_func()
# console output: 'Judäische Volksfront'

#%%
# äußere Funktion definieren
def outer_func():
    
    # eine lokale im Scope outer_func definieren
    x = "Judäische Volksfront"

    # inner Funktion definieren
    def inner_func():
        
        # Variable in übergeordneten Scope zu überschreiben
        nonlocal x
        x = "Volksfront von Judäa"
    
    # innere Funktion innerhalb der äußeren Funktion aufrufen
    inner_func()
    
    return(x)

# äußere und darin enthaltene innere Funktion ausführen
outer_func()
# console output: 'Volksfront von Judäa'

#%%
# regulärer Funktionsdefinition
def sum_of_product(x, y):
    return(sum(x*y))

# Lambda-Funktion
lambda x, y: sum(x*y)

