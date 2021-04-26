# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Wissenschaftliche Berechnung
# NumPy, Pandas, SciPy


###### NumPy

#%%
# das Numpy-Package laden
import numpy as np

#%%
# die numpy-Version anzeigen lassen
print(np.__version__)
# console output: 1.19.2

#%%
# eine Liste erzeugen
my_list = [1, 2, 3, 4, 5]

# eine Liste in einen Numpy-Array konvertieren
my_array = a = np.array(my_list)

# Array in die Konsole ausgeben lassen
print(my_array)
# console output: [1 2 3 4 5]

# Datenstruktur überprüfen
isinstance(my_array, np.ndarray)
# console output: True

#%%
# Dimensionen des Arrays überprüfen
print(my_array.shape)
# console output: (5,)

#%%
# einen zwei-dimensionalen Array erzeugen
my_array_2 = np.array([[1,2,3], [4,5,6], [7,8,9]])

# Array in die Konsole ausgeben lassen
print(my_array_2)
# console output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Dimensionen des Arrays überprüfen
print(my_array_2.shape)
# console output:
# (3, 3)

#%%
# die Anzahl der Dimensionen des Arrays ausgeben
print(my_array_2.ndim)
# console output: 2

#%%
# die Anzahl der Elemente im Array ausgeben
print(my_array_2.size)
# console output: 9

#%%
# den Datentyp der im Array gespeicherten
# Werte ausgeben
print(my_array_2.dtype)
# console output: int32

#%%
# Versuch, Datentypen innerhalb eines Arrays zu mischen
my_array_3 = np.array([[1,2,3], [4,5,6], [7,8,"neun"]])

print(my_array_3)
# console output: 
# [['1' '2' '3']
#  ['4' '5' '6']
#  ['7' '8' 'neun']]

#%%
# einen Array aus einem Tupel erzeugen
my_array_4 = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# den erzeugten Array inspizieren
print(my_array_4)
# console output: [ 1  2  3  4  5  6  7  8  9 10]

print(my_array_4.shape)
# console output: (10,)

#%%
# den ein-dimansionalen Array in einen Array
# mit 5 Zeilen und 2 Spalten konvertieren
my_array_5 = my_array_4.reshape(5, 2)

# den neuen Array inspizieren
print(my_array_5)
# console output:
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]]

print(my_array_5.shape)
# console output: (5, 2)

#%%
# den Speicherplatz in Bytes ausgeben, den ein Element
# des Arrays belegt
print(my_array_5.itemsize)
# console output: 4

#%%
# die ID für den im RAM belegten Speicher ausgeben
print(my_array_5.data)
# console output: <memory at 0x00000203321B8AD0>

#%%
# zwei Arrays erzeugen anhand derer mathematische
# Berechnung getestet werden können
arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = np.array([6, 7, 8, 9, 10])

#%%
# einfache mathematische Berechnungen
# Addition
print(arr_1 + arr_2)
# console output: array([ 7,  9, 11, 13, 15])

# Subtraktion
print(arr_1 - arr_2)
# console output: [-5 -5 -5 -5 -5]

# Multiplikation
print(arr_1 * arr_2)
# console output: [ 6 14 24 36 50]

# Division
print(arr_1 / arr_2)
# console output: [0.16666667 0.28571429 0.375 0.44444444 0.5]

#%%
# einfache deskriptive Statistiken
# arithmetisches Mittel
print(np.mean(arr_1))
# console output: 3.0

# Median
print(np.median(arr_2))
# console output: 8.0

# Varianz
print(np.var(arr_1))
# console output: 2.0

# Standardabweichung
print(np.std(arr_1))
# console output: 1.4142135623730951

# Minimaler Wert
print(np.min(arr_1))
# console output: 1

# Maximaler Wert
print(np.max(arr_1))
# console output: 5

# Summe aller Werte
print(np.sum(arr_1))
# console output: 15

# Summe aller Werte, die größer sind als das
# arithmetische Mittel
print(sum(arr_1 > np.mean(arr_1)))
# console output: 2

#%%
# Zufallszahlen generieren
my_array_6 = np.random.randn(5)
print(my_array_6)
# console output: array([-0.58036192, -0.68548047, \
# 0.29878082,  0.51872387, -2.51121088])


###### Pandas

#%%
# packages laden
import pandas as pd
import numpy as np
print(pd.__version__)
# console output: 1.1.3

#%%
# zwei Series erzeugen
my_series_1 = pd.Series(np.random.randn(5))
my_series_2 = pd.Series(np.random.randn(5))

#%%
# Series spaltenweise zu einem Dataframe verketten
my_df_1 = pd.concat([my_series_1, my_series_2], axis=1)

# Dataframe anzeigen
print(my_df_1)
# console output: 
#           0         1
# 0  1.462723  0.567359
# 1 -0.236114  0.485742
# 2 -0.232672  0.681681
# 3 -0.235927 -0.217541
# 4  1.322616 -2.842729

# überprüfen, ob es sich um einen Dataframe
# handelt
print(isinstance(my_df_1, pd.DataFrame))
# console output: True

#%%
# einen Dataframe aus einem Dictionary erzeugen
my_dic = {"Name":['Bernd', 'Silke', 'Claudia'], \
          "Alter":[54, 36, 23], \
          "Lieblingszahl":np.random.randn(3)}
my_df_2 = pd.DataFrame(my_dic)

# Dataframe anzeigen
print(my_df_2)
# console output: 
#       Name  Alter  Lieblingszahl
# 0    Bernd     54      -1.504067
# 1    Silke     36       1.832141
# 2  Claudia     23      -0.410978 

#%%
# Dataframe mit anderem Index erzeugen
my_df_3 = pd.DataFrame(my_dic, \
    index=['1001', '1002', '1003'])

# Dataframe anzeigen
print(my_df_3)
# console output: 
#          Name  Alter  Lieblingszahl
# 1001    Bernd     54      -1.504067
# 1002    Silke     36       1.832141
# 1003  Claudia     23      -0.410978

# Index anzeigen
print(my_df_3.index)
# console output:
# Index(['1001', '1002', '1003'], dtype='object')

#%%
# Daten aus einer CSV-Datei in einen Dataframe laden
dat = pd.read_csv('sample_data.csv')

# Dataframe anzeigen
print(dat)
#    place  min  max        type public      date      fee resp
# 0    NaN  2.1  4.8        trad   True       NaN  £200.45   CT
# 1    NaN  NaN  3.2         NaN  False  1/1/2017  £150.38   AS
# 2   25.0  2.3  3.3     forrest   True  2/1/2017   £85.07   CT
# 3   35.0  2.4  NaN        trad    NaN  3/1/2017      NaN   CT
# 4    NaN  2.1  4.8        trad   True       NaN  £200.45   CT
# 5   12.0  NaN  3.3     waldorf  False  2/1/2017  £350.96   AS
# 6   18.0  2.5  NaN     forrest    NaN  4/1/2017      NaN   CT
# 7   15.0  2.3  4.3  montessori   True  2/1/2017   £85.07   CT

#%%
# Datenform anzeigen
dat.shape
# console output: (8, 8)

#%%
# Informationen zum Datenobjekt anzeigen
dat.info()

# console output: 
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 8 entries, 0 to 7
# Data columns (total 8 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   place   5 non-null      float64
#  1   min     6 non-null      float64
#  2   max     6 non-null      float64
#  3   type    7 non-null      object 
#  4   public  6 non-null      object 
#  5   date    6 non-null      object 
#  6   fee     6 non-null      object 
#  7   resp    8 non-null      object 
# dtypes: float64(3), object(5)
# memory usage: 640.0+ bytes

#%%
# deskriptive Statistiken für nummerische Spalten anzeigen
dat.describe()

# console output: 
#       place      	min     	max
# count	5.000000	6.000000	6.000000
# mean	21.000000	2.283333	3.950000
# std	9.192388	0.160208	0.771362
# min	12.000000	2.100000	3.200000
# 25%	15.000000	2.150000	3.300000
# 50%	18.000000	2.300000	3.800000
# 75%	25.000000	2.375000	4.675000
# max	35.000000	2.500000	4.800000

#%%
# Anzahl der vorkommenden Werte pro Spalte anzeigen
dat["resp"].value_counts()

# console output: 

# Anzahl der vorkommenden Werte pro Spalte anzeigen...
# CT    6
# AS    2
# Name: resp, dtype: int64

#%%
# Anzahl der fehlenden Werte anzeigen
dat.isna().sum()

# console output: 
# place     3
# min       2
# max       2
# type      1
# public    2
# date      2
# fee       2
# resp      0
# dtype: int64

#%%
# auf eine Spalte/Series zugreifen
dat['fee']
# console output: 
# 0    £200.45
# 1    £150.38
# 2     £85.07
# 3    £250.00
# 5    £350.96
# 6    £250.00
# 7     £85.07
# Name: fee, dtype: object

#%%
# auf einen bestimten Eintrag zugreifen
dat.loc[2, 'type']
# console output: 'forrest'

#%%
# auf einen bestimmten Eintrag über Index zugreifen
dat.iloc[2, 3]
# console output: 'forrest'

#%%
# auf einen bestimmten Bereich zugreifen
dat.iloc[2:5, 3:6].values
# console output: 
# array([['forrest', True, '2/1/2017'],
#        ['trad', nan, '3/1/2017'],
#        ['trad', True, nan]], dtype=object)

#%%
# duplizierte Zeilen anzeigen
dat.duplicated()

# console output: 
# 0    False
# 1    False
# 2    False
# 3    False
# 4     True
# 5    False
# 6    False
# 7    False
# dtype: bool

# duplizierte Zeilen entfernen
dat = dat.drop_duplicates()

#%%
# spaltenweise definieren, wie fehlende Werte
# ersetzt werden sollen
fill_values = {'place':np.nanmedian(dat['place']), \
    'min':np.mean(dat['min']),
    'max':np.mean(dat['max']), \
    'type': 'trad', \
    'public':True, \
    'date':'1/1/2017',
    'fee':'£250.00'}

# fehlende Werte ersetzen
dat.fillna(value=fill_values, inplace=True)

# resultierenden Dataframe anzeigen
dat
# console output: 
# 	place	min	    max	    type	    public	date	    fee	    resp
# 0	18.0	2.10	4.80	trad	    True	1/1/2017	£200.45	CT
# 1	18.0	2.32	3.20	trad        False	1/1/2017	£150.38	AS
# 2	25.0	2.30	3.30	forrest	    True	2/1/2017	£85.07	CT
# 3	35.0	2.40	3.78	trad	    True	3/1/2017	£250.00	CT
# 5	12.0	2.32	3.30	waldorf	    False	2/1/2017	£350.96	AS
# 6	18.0	2.50	3.78	forrest	    True	4/1/2017	£250.00	CT
# 7	15.0	2.30	4.30	montessori	True	2/1/2017	£85.07	CT

#%%
# Pfundzeichen in 'fee'-Spalte entfernen
# und nach 'float' konvertieren
dat['fee'] = dat['fee'].\
    map(lambda x: str(x)[1:]).\
        astype('float')

# resultierenden Dataframe anzeigen
dat
# console output: 
#   place	min	    max	    type	    public	date	    fee	    resp
# 0	18.0	2.10	4.80	trad	    True	1/1/2017	200.45	CT
# 1	18.0	2.32	3.20	trad	    False	1/1/2017	150.38	AS
# 2	25.0	2.30	3.30	forrest	    True	2/1/2017	85.07	CT
# 3	35.0	2.40	3.78	trad	    True	3/1/2017	250.00	CT
# 5	12.0	2.32	3.30	waldorf	    False	2/1/2017	350.96	AS
# 6	18.0	2.50	3.78	forrest	    True	4/1/2017	250.00	CT
# 7	15.0	2.30	4.30	montessori	True	2/1/2017	85.07	CT

#%%
# Werte ersetzen
rep_dic = {'CT':'City', 'AS':'Ass.'}
dat.replace(to_replace = rep_dic, inplace=True)

# resultierenden Dataframe anzeigen
dat
# console output: 
# 	place	min	    max	    type	    public	date    	fee 	resp
# 0	18.0	2.10	4.80	trad	    True	1/1/2017	200.45	City
# 1	18.0	2.32	3.20	trad	    False	1/1/2017	150.38	Ass.
# 2	25.0	2.30	3.30	forrest	    True	2/1/2017	85.07	City
# 3	35.0	2.40	3.78	trad	    True	3/1/2017	250.00	City
# 5	12.0	2.32	3.30	waldorf	    False	2/1/2017	350.96	Ass.
# 6	18.0	2.50	3.78	forrest 	True	4/1/2017	250.00	City
# 7	15.0	2.30	4.30	montessori	True	2/1/2017	85.07	City

#%%
# Dataframe als CSV-Datei speichern
dat.to_csv('preprocessed_data.csv', encoding="utf-8")

###### SciPy

#%%
# Module laden
import numpy as np
from scipy.special import jn, yn, jn_zeros, yn_zeros
from scipy.integrate import quad, dblquad, tplquad
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import random as rand

#%%
# Berechnung von Besselfunktionen erster Art
alpha = 0
x = 0.0
print("Besselfunktion erster Art")
jn(alpha, x)
# console output: 1.0

#%%
# Berechnung von Besselfunktionen zweiter Art
x = 1.0
print("Besselfunktion zweiter Art")
yn(alpha, x)
# console output: 0.08825696421567697

#%%
# vier Bessel-Funktionen aufzeichnen
x = np.linspace(0, 10, 100)
fig, ax = plt.subplots()
for alpha in range(4):
    ax.plot(x, jn(alpha, x), label=r"J$_{}(x)$".format(alpha))
    ax.legend();
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Bessel Functions")
plt.show()

#%%
# Definitives Integral berechnen
a = 0
b = 1
integral_value, absolute_error = quad(np.cos, a, b)
print('Integralwert:', integral_value)
print('Absoluter Fehler', absolute_error)

# console output: 
# Integralwert: 0.8414709848078965
# Absoluter Fehler 9.34220461887732e-15

#%%
# Interpolation linearer und kubischer Funktionen

# Wertebereiche generieren
n = np.arange(0, 10)
x = np.linspace(0, 9, 100)

# die tatsächlichen Werte berechnen
y_actual = np.cos(x)

# zufällige Versuchsdaten erzeugen
y_experiment = np.cos(n) + 0.1 * np.random.randn(len(n))

#%%
# lineare Interpolation durchführen
linear_interpolation = interp1d(n, y_experiment, kind="linear")
y_linear_interpolation = linear_interpolation(x)

#%%
# kubische Interpolation durchführen
cubic_interpolation = interp1d(n, y_experiment, kind="cubic")
y_cubic_interpolation = cubic_interpolation(x)

#%%
# Vergleichsplot erzeugen
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(n, y_experiment, "bs", label="experiment data")
ax.plot(x, y_actual, "k", lw=2, label="actual function")
ax.plot(x, y_linear_interpolation, "r", label="linear interpolation")
ax.plot(x, y_cubic_interpolation, "g", label="cubic interpolation")
ax.legend(loc=3);
plt.xlabel("x")
plt.ylabel("y")
plt.title("Functions Interpolation Example")
plt.show()

