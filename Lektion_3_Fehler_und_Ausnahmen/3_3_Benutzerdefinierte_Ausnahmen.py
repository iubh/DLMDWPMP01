# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Benutzerdefinierte Ausnahmen

#%%
# eine eigene Exception-Klasse definieren
class RomanError(Exception):
    
    # einen Konstruktur definieren
    def __init__(self):
        
        # eine eigene Nachricht als Attribut definieren
        my_message = 'Die Römer haben nichts für uns getan'
        self.my_message = my_message


#%%
# eine Funktion definieren, die von der eigenen Exception-
# Klasse Gebrauch macht
def roemer_taten(x):

    # versuche die folgenden Anweisungen auszuführen
    try:
    
        # eine Liste zur Prüfung einer Kondition generieren
        done = ["Kanalisation", "Medizinische Versorgung", \
            "Bildung", "Wein", "Öffentliche Ordnung", \
            "Bewässerung", "Straßen", "Trinkwassersystem",
            "öffentliches Gesundheitswesen"]

        # eine Kondition testen
        if x in done:
            
            # wenn sich das Argument, was der Funktion übergeben
            # wurde, in der Liste befindet, wird kein Fehler
            # ausgelöst und der folgende String ausgegeben
            print("Ok, abgesehen von " + ", ".join(done), \
                "...was haben die Römer je für uns getan?")
        
        # wenn sich das Argument, was der Funktion übergeben
        # wurde, nicht in der Liste befindet, wird die
        # eigens definierte Exception geworfen
        else:
            raise RomanError
        
    # einen Exception Handler für die eigene Exception
    # definieren
    except RomanError:
        print(RomanError().my_message)


#%%
# die Funktion aufrufen, ohne dass ein
# Fehler ausgelöst wird
roemer_taten('Wein')

# console output:
# Ok, abgesehen von Kanalisation, Medizinische Versorgung,
# Bildung, Wein, Öffentliche Ordnung, Bewässerung, Straßen,
# Trinkwassersystem, öffentliches Gesundheitswesen
# ...was haben die Römer je für uns getan?

#%%
# die Funktion aufrufen, sodass ein
# Fehler ausgelöst wird
roemer_taten('Bowlingbahn')

# console output:
# Die Römer haben nichts für uns getan

# %%
