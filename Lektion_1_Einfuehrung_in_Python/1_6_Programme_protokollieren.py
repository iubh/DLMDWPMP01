# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Programme protokollieren

#%%
# logging-Funktionalitäten laden
import logging

# Logging-Nachrichten mit unterschiedlichen Levels
# der Ereignisschwere erzeugen
logging.debug("Nachricht an mich selbst: Besser bitte")
logging.info("Dies ist ein Test-Skript")
logging.warning("Der Kaffee ist fast leer")
logging.error("Der Kaffee ist leer")
logging.critical("Die Kaffeemaschine ist kaputt")

# console output: 
# WARNING:root:Der Kaffee ist fast leer
# ERROR:root:Der Kaffee ist leer
# CRITICAL:root:Die Kaffeemaschine ist kaputt

#%%
import logging

# Logging-Configuration einstellen
logging.basicConfig(level=logging.DEBUG)

# Debugging-Nachricht loggen
logging.debug("Nachricht an mich selbst: Besser bitte")

# console output:
# DEBUG:root:Nachricht an mich selbst: Besser bitte

#%%
import logging

# logging-Datei spezifizieren
logging.basicConfig(filename="my_log_1.log", filemode="w")

# logging-Nachricht in die logging-Datei schreiben
logging.warning("Der Kaffee ist fast leer")

#%%
import logging

# logging-Datei spezifizieren
logging.basicConfig(filename="my_log_2.log", filemode="w", \
            format="%(process)d-%(levelname)s-%(message)s")

# logging-Nachricht in die logging-Datei schreiben
logging.warning("Der Kaffee ist fast leer")

#%%
import logging

# logging-Datei spezifizieren
logging.basicConfig(filename="my_log_3.log", filemode="w", \
                    format="%(asctime)s - %(message)s")

# logging-Nachricht in die logging-Datei schreiben
logging.warning("Der Kaffee ist fast leer")

#%%
import logging

# logging-Datei spezifizieren
logging.basicConfig(filename="my_log_3.log", filemode="a")

# eine Variable definieren
item = 'Kaffemaschine'

# logging-Nachricht in die logging-Datei schreiben
logging.critical('%s hat einen kritischen Fehler verursacht',\
    item)