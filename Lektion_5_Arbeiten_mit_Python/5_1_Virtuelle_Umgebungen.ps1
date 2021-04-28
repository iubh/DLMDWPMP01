# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Virtuelle Umgebungen

## venv

# eine virtuelle Umgebung mit venv erstellen
python -m venv E:\my_env

# diese ve aktivieren
E:\my_env\Scripts\activate.bat

## conda

# Version überprüfen
conda --version
# console output: conda 4.9.2

# weite Informationen anzeigen
conda info

# Conda aktualisieren
conda update conda

# base-Umgebung aktualisieren
conda update -n base -c defaults conda

# eine neue Umgebung auf Basis der
# base-Umgebung erzeugen
conda create --clone base --name testenv

# eine virtuelle Umgebung von Scratch erzeugen
conda create --name oldPython python=3.7

# verfügbare virtuelle Umgebungen auflisten
conda env list

# virtuelle Umgebung aktivieren
conda activate oldPython

# die in dieser Umgebung installierten
# Bibliotheken anzeigen
conda list

# Bibliotheken installieren
conda install numpy
conda install pandas
conda install scipy
conda install statsmodels
conda install scikit-learn
conda install matplotlib
conda install seaborn

# Abhängigkeiten in einer YAML-Datei speichern
conda env export --name oldPython > program_requirements.yml

# eine virtuelle Umgebung löschen
conda activate base
conda remove --name oldPython --all

# eine neue virtuelle Umgebung anhand einer
# YAML-Datei erzeugen
conda env create --file program_requirements.yml

# aufräumen - virtuelle Test-Umgebungen löschen
conda remove --name oldPython --all
conda remove --name testenv --all