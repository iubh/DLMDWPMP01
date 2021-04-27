# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# Zugriff auf Datenbanken

## mit einer MySQL-Datenbank verbinden

#%%
# Bibliotheken laden
import sqlalchemy as db
import os

# Bibliotheksversionen anzeigen
print('SQLAlchemy-Version: ', db.__version__)

#%%
# ein Engine-Objekt erzeugen
my_password = os.getenv('MYPASSWORD')
con_str = "mysql+pymysql://chris:" + my_password + "@localhost/movie"
engine = db.create_engine(con_str)

# ein DB-Verbindungsobjekt erzeugen
connection = engine.connect()

# ein Metadaten-Objekt erzeugen
meta_data = db.MetaData()

## Tabelle erstellen

#%%
# Entwurfsskript für "actor"-Tabelle
actor = db.Table(
    "actor", meta_data,
    db.Column("id", db.Integer, primary_key=True, \
        autoincrement=True, nullable=False),
    db.Column("first_name", db.String(50), nullable=False),
    db.Column("last_name", db.String(50), nullable=False),
    db.Column("age", db.Integer, nullable=False),
    db.Column("date_of_birth", db.Date, nullable=False),
    db.Column("active", db.Boolean, nullable=False))

# "actor"-Tabelle erstellen und Informationen im 
# Metadaten-Objekt speicher
meta_data.create_all(engine)

## Daten einfügen

#%%
# Insert-Anweisung erzeugen
sql_query = db.insert(actor)

# eine Liste aus Dictionary-Einträgen erstellen
data_list = [{"first_name":"John", "last_name":"Smith", \
    "age":50, "date_of_birth":"1969-04-05", "active":True}, \
        {"first_name":"Brian", "last_name":"Morgan", \
    "age":38, "date_of_birth":"1981-02-11", "active":True}, \
        {"first_name":"David", "last_name":"White", \
    "age":77, "date_of_birth":"1942-06-30", "active":False}]

# Insert-Anweisung ausführen
result = connection.execute(sql_query, data_list)

## Daten abfragen

#%%
# Selektor generieren
sel = db.select([actor])

# Selektion durchführen
query_result_1 = connection.execute(sel)

# alle Zeilen des Abfrageergebnisses iterativ
# ausgeben
for row in query_result_1:
    print(row)

# console output:
# (1, 'John', 'Smith', 50, datetime.date(1969, 4, 5), True)
# (2, 'Brian', 'Morgan', 38, datetime.date(1981, 2, 11), True)
# (3, 'David', 'White', 77, datetime.date(1942, 6, 30), False)

#%%
# Selektor generieren
sel = db.select([actor.c.first_name, actor.c.last_name])

# Selektion durchführen
query_result_2 = connection.execute(sel)

# alle Zeilen des Abfrageergebnisses iterativ
# ausgeben
for row in query_result_2:
    print(row)

# console output:
# ('John', 'Smith')
# ('Brian', 'Morgan')
# ('David', 'White')

#%%
# Selektor generieren
sel = db.select([actor.c.first_name, actor.c.last_name]).\
    where(actor.c.active == 1)

# Selektion durchführen
query_result_3 = connection.execute(sel)

# alle Zeilen des Abfrageergebnisses iterativ
# ausgeben
for row in query_result_3:
    print(row)

# console output:
# ('John', 'Smith')
# ('Brian', 'Morgan')

## Daten aktualisieren

#%%
# ein Update-Statement erzeugen
sql_query = db.update(actor).values(active=False).\
    where(actor.c.id==2)

# Update durchführen
updated = connection.execute(sql_query)

## Daten löschen

# %%
# Statement zur Löschung eines Eintrages erstellen
sql_query = db.delete(actor).where(actor.c.id==1)

# Statement ausführen
deletion_result = connection.execute(sql_query)
