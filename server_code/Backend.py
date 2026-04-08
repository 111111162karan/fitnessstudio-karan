import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

@anvil.server.callable
def sql_query(query):
  with sqlite3.connect(data_files("Karan_Özcelik_fitnessstudio.db")) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

@anvil.server.callable
def Get_Startseite_Data():
  sql_query("""
  SELECT 
    k.KID,
    k.Bezeichnung,
    k.Wochentag,
    k.Uhrzeit,
    t.Vorname || ' ' || t.Nachname AS Trainer,
    COUNT(a.AID) AS Teilnehmer,
    k.Max_Teilnehmer
  FROM Kurs k
  LEFT JOIN Trainer t ON k.TID = t.TID
  LEFT JOIN Anmeldung a ON k.KID = a.KID
  GROUP BY k.KID;
  """)
  

    


