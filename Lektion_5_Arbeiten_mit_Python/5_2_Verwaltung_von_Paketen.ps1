# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Verwaltung von Paketen

## Pakete mit pip verwalten

# pip-Version anzeigen
pip --version
# console output:
# pip 20.2.4 from C:\Users\chris\anaconda3\lib\site-packages\pip (python 3.8)

# Schnellhilfe zu pip-Befehlen anzeigen
pip help

# pip aktualisieren
python -m pip install --upgrade pip
# console output: Successfully installed pip-21.1

# die in der aktiven Umgebung installierten Pakete anzeigen
pip list

# ein Paket mit pip installieren
pip install seaborn

# ein Paket aktualisieren
pip install --upgrade numpy

# ein Paket deinstallieren
# pip uninstall scikit-learn

# nähere Informationen zu einem installierten Paket erhalten
pip show pandas

# console output:
# Name: pandas
# Version: 1.1.3
# Summary: Powerful data structures for data analysis, time series, and statistics
# Home-page: https://pandas.pydata.org
# Author: None
# Author-email: None
# License: BSD
# Location: c:\users\chris\anaconda3\lib\site-packages
# Requires: numpy, python-dateutil, pytz
# Required-by: statsmodels, seaborn

## Pakete mit conda verwalten
conda --version
# console output: conda 4.10.1

# Schnellhilfe zu conda-Befehlen anzeigen
conda help

# conda aktualisieren
conda update conda

# ein Paket mit conda installieren
conda install seaborn

# die in der aktiven Umgebung installierten Pakete anzeigen
conda list

# ein Paket aktualisieren
conda update numpy

# ein Paket deinstallieren
# conda uninstall scikit-learn

# nach einem Paket in den für conda eingestellten
# Quellen suchen
conda search pandas
