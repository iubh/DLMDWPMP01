# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Behandlung und Auslösung von Ausnahmen

#%%
# eine Funktion mit exception handler definieren
def handle_exceptions():

     try:
         # Funktionscode
         pass
     
     except:
         # Ausnahmen abfangen und behandeln
         pass

     finally:
         # Dieser Block wird immer ausgeführt.
         pass

#%%
# module laden
import traceback
from datetime import datetime

# eine Funktion mit exception handler definieren
def my_division(x, y):
    
    # Division versuchen
    try:
        output = x/y
        return(output)
    
    # mögliche Exception behandeln
    except:
        
        # Angaben zum Zeitpunkt des Fehlers ausgeben
        now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        print("Exception Datetime:", now)
        
        # Fehler abfangen
        exception_type, exception_value, \
            exception_traceback = sys.exc_info()
        
        # exception_type und value ausgeben
        print("Exception Type:", exception_type)
        print("Exception Value:", exception_value)
         
        # traceback abfangen
        file_name, line_number, procedure_name, \
            line_code = traceback.\
                extract_tb(exception_traceback)[-1]
        
        # traceback informationen ausgeben
        print("File Name:",  file_name)
        print("Line Number:",  line_number)
        print("Procedure Name:",  procedure_name)
        print("Line Code:",  line_code)

    finally:
        print("The function ran until the end.")

#%%
# Funktion mit ausführbaren Argumenten testen
my_division(10, 2)

# console output:
# The function ran until the end.
# 5.0

#%%
# Null-Division testen
my_division(10, 0)

# console output:
# Exception Datetime: 15-04-2021 11:16:47 AM
# Exception Type: <class 'ZeroDivisionError'>
# Exception Value: division by zero
# File Name: <ipython-input-9-0dd947a226ab>
# Line Number: 9
# Procedure Name: my_division
# Line Code: output = x/y
# The function ran until the end.

#%%
# eine Funktion mit exception handler definieren
def handle_exceptions():
    
    try:
        # Funktionscode
        pass
     
    except <ExceptionError1>:
        # Ausnahmen abfangen und behandeln, die sich
        # auf ExceptionError1 beziehen
        pass

    except <ExceptionError2>:
        # Ausnahmen abfangen und behandeln, die sich
        # auf ExceptionError2 beziehen
        pass
    
    else:
        # Anweisungen, die nur dann ausgeführt werden,
        # wenn im try-Block kein Fehler aufgetreten ist
        pass

    finally:
        # Dieser Block wird immer ausgeführt.
        pass


#%%
# eine Funktion mit exception handler definieren
def my_division(x, y):
    
    # Division versuchen
    try:
        
        # einen Fehler bei Eingabe eines negativen
        # Wertes ausgeben
        if x < 0:
            raise ValueError("es sind nur \
                positive Werte erlaubt")
        
        output = x/y
    
    # mögliche Exception behandeln
    except ValueError:
        print("Es wurde ein unzulässiger Wert eingegeben")
    
    except ZeroDivisionError:
        print("Es wurde versucht durch 0 zu teilen")
    
    else:
        print("Super! Die Berechnung hat \
            keine Fehler verursacht")
        return(output)

    finally:
        print("Die Funktion hat ihr Ende erreicht.")


#%%
# die Funktion mit zulässigen Argumenten ausführen
my_division(10,5)

# console output:
# Super! Die Berechnung hat keine Fehler verursacht
# Die Funktion hat ihr Ende erreicht.
# 2.0

#%%
# Funktion mit negativem Wert ausführen
my_division(-10, 2)

# console ouput:
# Es wurde ein unzulässiger Wert eingegeben
# Die Funktion hat ihr Ende erreicht.

#%%
# durch 0 teilen
my_division(10, 0)

# console ouput:
# Es wurde versucht durch 0 zu teilen
# Die Funktion hat ihr Ende erreicht.
