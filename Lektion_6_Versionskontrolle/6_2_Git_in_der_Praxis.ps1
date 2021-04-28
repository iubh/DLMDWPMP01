# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Git in der Praxis


# ein Remote Repository klonen
git clone <Remote-Repository-URL>

# ein Remote Repository mit Credentials klonen
git clone <username>@<host>:<Remote-Repository-URL>

# lokales Repository erstellen
git init

# ein lokales repo mit einem remote repo verbinden
git remote add origin <Remote-Repository-URL>

# Änderungen in einer Datei stagen
git my_modified_code.py

# alle Änderungen stagen
git add *

# Änderungen commiten
git commit -m "Tests für die Divisionsfunktion hinzugefügt"

# Änderungen in der gleiche Ausgangsrepo
# und in den Master-Branch pushen
git push origin master

# Kurzform des oberen Befehls mit Standardangaben
git push

# neuen Branch erstellen und dorthin wechseln
git checkout -b <branch_name>

# zurück zum Master-Branch wechseln
git checkout master

# einen Branch löschen
git branch -d <branch_name>

# explizit in einen bestimmten Branch pushen
git push origin <branch_name>

# den neusten Stand aus dem Remote Repository beziehen
git pull

# einen anderen Branch mit dem aktiven Branch verschmelzen
git merge <branch_name>

# erneutes stagen von manuell modifizierten Datein
git add <filename>

# Differenzen zwischen zwei Branches anzeigen
git diff <source_branch> <target_branch>

# einen commit mit einem tag versehen
git tag 1.2.0 1b1e3d655ff

# Repo-Historie anzeigen
git log

# nach geänderten Datein filtern
git log --name-status

# nur Commits eines bestimmten Autor anzeigen
git log --author=chris

# komprimiertes Commit-History anzeigen
git log --pretty=oneline

# einen Strukturbaum der Branches und Commits anzeigen
git log --graph --oneline --decorate --all

# Hilfe zu Befehlen mit Bezug auf die Commit-Historie anzeigen
git help -a log

# allgemeine Schnellhilfe zu Git anzeigen
git help

# lokale Änderungen in einer Datei verwerfen
git checkout --<filename>

# alle lokalen Änderungen und Commits verwerfen
git fetch origin
git reset --hard origin/master
