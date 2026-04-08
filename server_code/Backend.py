import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

@anvil.server.callable
def sql_query(query):
  with sqlite3.connect(data_files["Özcelik_Karan_fitnessstudio.db"]) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
  return result

@anvil.server.callable
def Get_Startseite_Data():
  return sql_query("""
  SELECT 
    k.KID,
    k.Wochentag,
    k.Uhrzeit,
    t.Vorname AS Trainer,
    t.Nachname AS Trainer,
    COUNT(a.AID) || '/' || k.Max_Teilnehmer AS Teilnehmer
    FROM Kurs k
    LEFT JOIN Trainer t ON k.TID = t.TID
    LEFT JOIN Anmeldung a ON k.KID = a.KID
    GROUP BY k.KID;
      """)

@anvil.server.callable
def get_verfuegbare_mitglieder(kid):
  with sqlite3.connect(data_files["Özcelik_Karan_fitnessstudio.db"]) as conn:
    cursor = conn.cursor()
    cursor.execute("""SELECT m.MID, m.Vorname, m.Nachname
                      FROM Mitglied m
                      WHERE m.MID NOT IN (
                          SELECT MID FROM Anmeldung WHERE KID = ?
                      )
                      """, (kid,))
    result = cursor.fetchall()
  return result
  

    


