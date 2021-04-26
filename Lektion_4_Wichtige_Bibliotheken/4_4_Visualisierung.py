# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Visualisierung

## Matplotlib

#%%
# Bibliotheken laden
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

#%%
# Daten generieren
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#%%
# Plot-Style definieren
style.use('ggplot')

### Line-Plot

#%%
# eine Plot-Figure mit einem Subplot (axes) erzeugen
fig, ax = plt.subplots(figsize=(6,4))

# einen Linienplot erzeugen
ax.plot(x, y, label="line plot example", linewidth=2)

# Legende hinzufügen
ax.legend()

# Grid hinzufügen
ax.grid(True,color="k")

# Achsen beschriften
plt.ylabel('y axis')
plt.xlabel('x axis')

# Titel hinzufügen
plt.title('Line Plot')

# Plot anzeigen
plt.show()


### Bar-Plot

#%%
# eine Plot-Figure mit einem Subplot (axes) erzeugen
fig, ax = plt.subplots(figsize=(6,4))

# einen Barplot erzeugen
ax.bar(x, y, label="bar chart vertical example", align='center')

# Legende hinzufügen
ax.legend()

# Grid hinzufügen
ax.grid(True,color="k")

# Achsenbeschriftungen hinzufügen
plt.ylabel('y axis')
plt.xlabel('x axis')

# Titel hinzufügen
plt.title('Bar Chart Vertical')

# Plot anzeigen
plt.show()

### Horizontaler Barplot

#%%
# eine Plot-Figure mit einem Subplot (axes) erzeugen
fig, ax = plt.subplots(figsize=(6,4))

# einen horizontalen Barplot erzeugen
ax.barh(x, y, label="bar chart horizontal example", align='center')

# Legende hinzufügen
ax.legend()

# Legende hinzufügen
ax.grid(True,color="k")

# Achsenbeschriftung hinzufügen
plt.ylabel('y axis')
plt.xlabel('x axis')

# Titel hinzufügen
plt.title('Bar Chart Horizontal')

# Plot anzeigen
plt.show()

### Scatter-Plot

#%%
# eine Plot-Figure mit einem Subplot (axes) erzeugen
fig, ax = plt.subplots(figsize=(6,4))

# einen Scatter-Plot erzeugen
ax.scatter(x, y, label="scatter plot example")

# Legende hinzufügen
ax.legend()

# Grid hinzufügen
ax.grid(True,color="k")

# Achsenbeschriftung hinzufügen
plt.ylabel('y axis')
plt.xlabel('x axis')

# Titel hinzufügen
plt.title('Scatter Plot')

# Plot anzeigen
plt.show()

### Histogramm

#%%
# normalverteilte Daten generieren
mu = 100
sigma = 15
x = mu + sigma * np.random.randn(10000)

# eine Plot-Figure mit einem Subplot (axes) erzeugen
fig, ax = plt.subplots(figsize=(6,4))

# ein Histogramm erzeugen
ax.hist(x, bins=50, density=True, facecolor='r', alpha=0.75, \
    label="histogram plot example")

# Text-Annotation hinzufügen (mathematische Notation)
ax.text(45, 0.028, r'$\mu=100,\ \sigma=15$')

# Werte-Bereiche der Axen einstellen
# [<x_min>, <x_max>, <y_min>, <y-max>]
ax.axis([40, 160, 0, 0.03])

# Legende hinzufügen
plt.legend()

# Grid hinzufügen
plt.grid(True,color="k")

# Achsenbeschriftung hinzufügen
plt.xlabel("x")
plt.ylabel("P(x)")

# Titel hinzufügen
plt.title("Histogram Plot")

# Plot anzeigen
plt.show()

## Seaborn

#%%
# Bibliotheken laden
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style

# Beispiel-Datensatz laden
iris_data = sns.load_dataset("iris")
iris_data

#%%
# den zu verwendenden Stil einstellen
style.use('ggplot')

### Swarm-Plot

# einen Swarm-Plot erstellen 
sns.swarmplot(x="species", y="petal_length", \
    data=iris_data)

# Achsen-Beschriftungen hinzufügen
plt.ylabel("petal length, cm")
plt.xlabel("species")

# einen Titel hinzufügen
plt.title("Species vs. Petal Length")

# den erzeugten Plot anzeigen
plt.show()

### Kategorie-Plot

#%%
# einen Kategorie-Plot erzeugen
sns.catplot(x="species", y="petal_length", \
    data=iris_data, kind="bar", palette="muted", \
        legend=False)

# Achsen beschriften
plt.ylabel("petal length, cm")
plt.xlabel("species")

# Titel hinzufügen
plt.title("Species vs. Petal Length")

# den erzeugten Plot anzeigen
plt.show()

### Box-Plot

#%%
# einen Box-Plot erzeugen
sns.boxplot(x="species", y="petal_length", \
    data=iris_data)

# Achsen beschriften
plt.ylabel("petal length, cm")
plt.xlabel("species")

# Titel hinzufügen
plt.title("Species vs. Petal Length")

# den erzeugten Plot anzeigen
plt.show()

#%%
# einen Pair-Plot
sns.pairplot(iris_data, hue="species", size=2)

# Achsen beschriften
plt.ylabel("petal length, cm")
plt.xlabel("species")

# den erzeugten Plot anzeigens
plt.show()


## Bokeh

#%%
# Bibliotheken laden
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.iris import flowers
import numpy as np

### Line-Plot

#%%
# Beispiel-Daten generieren
x = [1, 2, 3, 4, 5]
y = [5, 6, 1, 3, 4]

#%%
# Ausgabe-Datei spezifizieren
output_file("line_example.html")

# eine "figure" erzeugen
plot = figure(title="Line Plot", x_axis_label="x axis", \
    y_axis_label="y axis")

# einen Linienplot erstellen
plot.line(x, y, legend="line example", line_width=2)

# erzeugten Plot anzeigen
show(plot)

### Sctter-Plot 1

#%%
# Beispiel-Daten generieren
x = np.linspace(-6, 6, 100)
y = np.cos(x)

#%%
# Ausgabe-Datei spezifizieren
output_file("cosx_example.html")

# eine "figure" erzeugen
plot = figure(width=500, height=500, title="Cos(x) Plot", \
    x_axis_label="x axis", y_axis_label="y axis")

# einen Circle-Plot erzeugen
plot.circle(x, y, size=7, color="firebrick", \
    alpha=0.5, legend="cos(x) example")

# erzeugten Plot anzeigen
show(plot)

### Bar-Plot

#%%
# Beispiel-Daten generieren
teams = ["A", "B", "C", "D", "E", "F"]
score = [4, 2, 3, 1, 3, 5]

# Ausgabe-Datei spezifizieren
output_file("barchart_example.html")

# eine "figure" erzeugen
plot = figure(x_range=teams, height=500, \
    title="Bar Chart Plot", x_axis_label="teams", \
        y_axis_label="values")

# vertikale Balken hinzufügen
plot.vbar(x=teams, top=score, \
    width=0.6, legend="bar chart example")

# erzeugten Plot anzeigen
show(plot)

### Scatter-Plot 2

#%%
# Farben für den Iris-Datensatz generieren
colormap = {"setosa":"red", "versicolor":"green", \
    "virginica":"blue"}
colors = [colormap[x] for x in flowers['species']]

# Ausgabe-Datei spezifizieren
output_file("iris_scatter_example.html")

# eine "figure" erzeugen
plot = figure(title = "Iris Flowers Scatter Plot", \
    x_axis_label="petal length", y_axis_label="petal width")

# einen Circle-Plot erzeugen
plot.circle(flowers["petal_length"], \
    flowers["petal_width"], color=colors, \
        fill_alpha=0.2, size=10, \
            legend="scatter plot example")

# erzeugten Plot anzeigen
show(plot)

