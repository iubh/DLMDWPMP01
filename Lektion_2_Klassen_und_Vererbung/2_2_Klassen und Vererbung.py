# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Klassen und Vererbung

#%%
# eine Fahrzeuge-Klasse definieren
class Vehicle():
    n_wheels = 4
    current_speed = 0.0

#%%
# ein PKW-Objekt generieren
car = Vehicle()

#%%
# ein Attribut des Objektes abfragen
print(car.n_wheels)
# console output: 4

#%%
# alle Attribute und Methoden des Objektes abfragen
dir(car)
# console output (extract):
# ['__class__',
# ...
# 'current_speed',
# 'n_wheels'] 

#%%
# ein weiteres Fahrzeug-Objekt generieren
bike = Vehicle()
print(bike.n_wheels)
# console output: 4

#%%
# ein Attribut des Objektes ändern
bike.n_wheels = 2
print(bike.n_wheels)
# console output: 2

print(car.n_wheels)
# console output: 4

#%%
# Namespace des Fahrrads betrachten
print(bike.__dict__)
# console output: {'n_wheels': 2}

#%%
# Namespace des PKW's betrachten
print(car.__dict__)
# console output: {}


#%%
# ein Klassen-Attribut ändern
Vehicle.n_wheels = 2
print("Car Wheels: " + str(car.n_wheels))
print("Bike Wheels: " + str(bike.n_wheels))
# console output:
# Car Wheels: 2
# Bike Wheels: 2

#%%
# Klassen-Attribut für Fahrzeuge zurücksetzen
Vehicle.n_wheels = 4


#%%
# andere Instanzen der Klasse bleiben unberührt
print(car.n_wheels)
# console output: 4

#%%
# der Klasse eine Methode hinzufügen
class Vehicle():
    
    n_wheels = 4
    current_speed = 0.0

    # Methode zur Beschleunigung hinzufügen
    def increase_speed(self, increment=5.0):
        self.current_speed += increment

#%%
# eine Instanz der Klasse generieren und aktuelle
# Geschwindigkeit ausgeben
bike = Vehicle()
print(bike.current_speed)
# console output: 0.0

#%%
# Die Geschwindigkeit um den Standardwert erhöhen
bike.increase_speed()
print(bike.current_speed)
# console output: 5.0

#%%
# die Geschwindigkeit um einen definierten Wert erhöhen
bike.increase_speed(7.0)
print(bike.current_speed)
# console output: 12.0

#%%
# Fahrzeug-Klasse mit Konstruktor-Methode definieren
class Vehicle():
    
    def __init__(self, n_wheels=4, current_speed=0.0):
        self.n_wheels = n_wheels
        self.current_speed = current_speed

#%%
# Objekte erzeugen
car = Vehicle()
bike = Vehicle(n_wheels=2)

# Instanz-Attribute überprüfen
print("Car Wheels: " + str(car.n_wheels))
print("Bike Wheels: " + str(bike.n_wheels))
# console output:
# Car Wheels: 4
# Bike Wheels: 2

#%%
class Vehicle():
    
    def __init__(self, n_wheels=None, current_speed=0.0):
        self.n_wheels = n_wheels
        self.current_speed = current_speed

#%%
# Objekte erzeugen
car = Vehicle()
bike = Vehicle(n_wheels=2)

# Instanz-Attribute überprüfen
print("Car Wheels: " + str(car.n_wheels))
print("Bike Wheels: " + str(bike.n_wheels))
# console output:
# Car Wheels: None
# Bike Wheels: 2

#%%
# eine PKW-Klasse defiinieren
class Car():

    # Konstruktor definieren
    def __init__(self, color, use_type):

        self.color = color
        self.use_type = use_type
        self.description = color + " " + use_type

#%%
# ein PKW-Objekt erzeugen
my_car = Car("blue", "family car")

#%%
# die Attribute des erzeugten Objektes ausgeben
print("Color:", my_car.color)
print("Use Type:", my_car.use_type)
print("Description:", my_car.description)
# console output:
# Color: blue
# Use Type: family car
# Description: blue family car

#%%
# das Farb-Attribut ändern
my_car.color = "pink"

print("Color:", my_car.color)
print("Use Type:", my_car.use_type)
print("Description:", my_car.description)
# console output:
# Color: pink
# Use Type: family car
# Description: blue family car

#%%
# PKW-Klasse erneut definieren
class Car():

    # Konstruktor definieren
    def __init__(self, color, use_type):

        self.color = color
        self.use_type = use_type
    
    # in einer Funktion die Beschreibung aus initierten
    # Attributen zusammensetzen
    def description(self):
        return self.color + " " + self.use_type

#%%
# erneut ein PKW-Objekt erzeugen
my_car = Car("blue", "family car")

# Attribute des Objektes anzeigen und Methode ausführen
print("Color:", my_car.color)
print("Use Type:", my_car.use_type)
print("Description:", my_car.description())
# console output:
# Color: blue
# Use Type: family car
# Description: blue family car

#%%
# das Farb-Attribut ändern
my_car.color = "pink"

# Attribute des Objektes anzeigen und Methode ausführen
print("Color:", my_car.color)
print("Use Type:", my_car.use_type)
print("Description:", my_car.description())
# console output:
# Color: pink
# Use Type: family car
# Description: pink family car

#%%
# PKW-Klasse erneut definieren
class Car():

    # Konstruktor definieren
    def __init__(self, color, use_type):

        self.color = color
        self.use_type = use_type
    
    # in einer Funktion die Beschreibung aus initierten
    # Attributen zusammensetzen und diese Funktion
    # als Attribut behandeln 
    @property
    def description(self):
        return self.color + " " + self.use_type

#%%
# erneut ein PKW-Objekt erzeugen
my_car = Car("blue", "family car")

# Attribute des Objektes anzeigen
print("Color:", my_car.color)
print("Use Type:", my_car.use_type)
print("Description:", my_car.description)
# console output:
# Color: blue
# Use Type: family car
# Description: blue family car

#%%
# das Farb-Attribut ändern
my_car.color = "pink"

# Attribute des Objektes anzeigen
print("Color:", my_car.color)
print("Use Type:", my_car.use_type)
print("Description:", my_car.description)
# console output:
# Color: pink
# Use Type: family car
# Description: pink family car

#%%
# Versuch, das zusammengesetzte Attribut zu ändern
my_car.description = "ocher van"
# console output: can't set attribute

#%%
# PKW-Klasse erneut definieren
class Car():

    # Konstruktor definieren
    def __init__(self, color, use_type):

        self.color = color
        self.use_type = use_type
    
    # in einer Funktion die Beschreibung aus initierten
    # Attributen zusammensetzen und diese als
    # Attribut behandeln
    @property
    def description(self):
        return self.color + ' ' + self.use_type

    # eine Setter-Methode zur Änderung von Attributen
    # auf Basis der Beschreibung definieren
    @description.setter
    def description(self, desc):
        color, use_type = desc.split(" ")
        self.color = color
        self.use_type = use_type

#%%
# erneut ein PKW-Objekt erzeugen
my_car = Car("blue", "family car")

#%%
# die Beschreibung ändern
my_car.description = "ocher van"

#%% Attribute anzeigen
print("Color:", my_car.color)
print("Use Type:", my_car.use_type)
print("Description:", my_car.description)
# console output:
# Color: ocher
# Use Type: van
# Description: ocher van

#%%
# Eine Sub-Klasse anlegen
class Car(Vehicle):
    pass

#%%
# eine Instanz der Subklasse erzeugen
mini_car = Car(n_wheels=4)

# vererbte Attribute betrachten
print("Anzahl Räder:", mini_car.n_wheels)
print("Momentane Geschwindigkeit:", mini_car.current_speed)
# console output:
# Anzahl Räder: 4
# Momentane Geschwindigkeit: 0.0

#%%
# Eine Sub-Klasse mit angepassten Attributen anlegen
class Car(Vehicle):
    
    # Konstruktor-Methode definieren
    def __init__(self, n_wheels=4, current_speed=0.0, \
        n_doors=3):
        
        # Konstruktor-Methode der Elternklasse ausführen
        Vehicle.__init__(self, n_wheels, current_speed)
        
        # angepasste Konstruktor-Methode der Kind-Klasse ausführen 
        self.n_doors = n_doors

#%%
# Instanzen der Subklasse erzeugen
mini_car = Car()
family_car = Car(n_doors=5)

# vererbte und angepasste Attribute betrachten
print("Mini-Car - Anzahl Räder:", mini_car.n_wheels)
print("Mini-Car - Momentane Geschwindigkeit:", \
    mini_car.current_speed)
print("Mini-Car - Anzahl Türen:", mini_car.n_doors)
print("Familiy-Car - Anzahl Räder:", family_car.n_wheels)
print("Familiy-Car - Momentane Geschwindigkeit:", \
    family_car.current_speed)
print("Familiy-Car - Anzahl Türen:", family_car.n_doors)

# console output: 
# Mini-Car - Anzahl Räder: 4
# Mini-Car - Momentane Geschwindigkeit: 0.0
# Mini-Car - Anzahl Türen: 3
# Familiy-Car - Anzahl Räder: 4
# Familiy-Car - Momentane Geschwindigkeit: 0.0
# Familiy-Car - Anzahl Türen: 5


#%%
# Vererbungsreihenfolge überprüfen
help(mini_car)
# extract from console output:
# Method resolution order:
#  |      Car
#  |      Vehicle
#  |      builtins.object


#%%
# überprüfen, ob ein Objekt eine Instanz einer Klasse ist
isinstance(mini_car, Car)
# console output: True

#%%
isinstance(mini_car, Vehicle)
# console output: True

#%%
# überprüfen, ob eine Klasse ein Kind einer Eltern-Klasse ist
issubclass(Car, Vehicle)
# console output: True

#%%
# Eltern-Klasse definieren
class Vehicle():
    
    # Konstruktor zur Generierung von Attributen
    def __init__(self, current_speed=0.0):
        self.current_speed = current_speed

    # Methode zur Beschleunigung hinzufügen
    def increase_speed(self, increment=5.0):
        self.current_speed += increment

#%%
# Kind-Klasse definieren
class Car(Vehicle):
    
    # Methoden-Überschreibung
    def increase_speed(self, increment=10.0):
        self.current_speed += increment

#%%
# eine weitere Kind-Klasse definieren
# Kind-Klasse definieren
class Bike(Vehicle):
    
    # Methoden-Überschreibung
    def increase_speed(self, increment=2.0):
        self.current_speed += increment

#%%
# zwei Objekte auf Basis der beiden Subklassen generieren
my_car = Car()
my_bike = Bike()

# beide Objekte 7-fach beschleunigen
for i in range(7):
    my_car.increase_speed()
    my_bike.increase_speed()

# aktuelle Geschwindigkeiten ausgeben
print("PKW-Geschwindigkeit:", my_car.current_speed)
print("Fahrrad-Geschwindigkeit:", my_bike.current_speed)
# console output:
# PKW-Geschwindigkeit: 60.0
# Fahrrad-Geschwindigkeit: 12.0

#%%
# eine Fahrzeug-Klasse definieren
class Vehicle():

    # Attribute per Konstruktor anlegen
    def __init__(self, n_wheels=4, increment=10, type="car"):

        # ein "öffentliches" Attribut anlegen
        self.n_wheels = n_wheels
        
        # ein "privates" Attribut anlegen
        self._increment = increment
        
        # ein "geschütztes" Attribut anlegen
        self.__type = type

# eine Instanz der Klasse erzeugen
my_car = Vehicle()

#%%
# "öffentliches" Attribut ausgeben
print(my_car.n_wheels)
# console output: 4

#%%
# "privates" Attribut ausgeben
print(my_car._increment)
# console output: 10 (funktioniert!)

#%%
# "geschütztes" Attribut ausgeben
print(my_car.__type)
# console output: 'Vehicle' object has no attribute '__type'

#%%
# Attribute und Methoden des Objektes anzeigen
dir(my_car)
# console output (extract):
# '_Vehicle__type',
# ...
#  '_increment',
#  'n_wheels']

#%%
# "geschütztes" Attribut ausgeben
# !!! ACHTUNG: NIEMALS AUF DIESE WEISE
# AUF EIN GESCHÜTZTES ATTRIBUT ZUGREIFEN !!!
print(my_car._Vehicle__type) # NIEMALS SO PROGRAMMIEREN !!!
# console output: car (funktioniert!)

#%%
# eine Fahrzeug-Klasse definieren
class Vehicle():

    # Attribute per Konstruktor anlegen
    def __init__(self, n_wheels=4, increment=10, type="car"):

        # ein "öffentliches" Attribut anlegen
        self.n_wheels = n_wheels
        
        # ein "privates" Attribut anlegen
        self._increment = increment
        
        # ein "geschütztes" Attribut anlegen
        self.__type = type

    # Setter für "geschützes" Attribut definieren
    def setType(self, type):
        self.__type = type
    
    # Getter für "geschützes" Attribut definieren
    def getType(self):
        print(self.__type)

# eine Instanz der Klasse erzeugen
my_car = Vehicle()


#%%
# auf "geschütztes" Attribut zugreifen
my_car.getType()
# console output: car