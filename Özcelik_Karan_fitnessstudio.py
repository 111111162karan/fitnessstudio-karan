import sqlite3

# Verbindung zur Datenbank herstellen (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect("Özcelik_Karan_fitnessstudio.db")
cursor = conn.cursor()


# Tabelle: Mitglied
cursor.execute("""
CREATE TABLE IF NOT EXISTS Mitglied (
    MID INTEGER PRIMARY KEY,
    Vorname TEXT,
    Nachname TEXT,
    Email TEXT,
    Beitrittsdatum DATE
);
""")

# Tabelle: Trainer
cursor.execute("""
CREATE TABLE IF NOT EXISTS Trainer (
    TID INTEGER PRIMARY KEY,
    Vorname TEXT,
    Nachname TEXT,
    Spezialgebiet TEXT
);
""")

# Tabelle: Kurs
cursor.execute("""
CREATE TABLE IF NOT EXISTS Kurs (
    KID INTEGER PRIMARY KEY,
    Bezeichnung TEXT,
    Wochentag TEXT,
    Uhrzeit TIME,
    Max_Teilnehmer INTEGER,
    TID INTEGER
);
""")

# Tabelle: Anmeldung
cursor.execute("""
CREATE TABLE IF NOT EXISTS Anmeldung (
    AID INTEGER PRIMARY KEY,
    MID INTEGER,
    KID INTEGER,
    Anmeldedatum DATE
);
""")


print("Datenbank und Tabellen wurden erfolgreich erstellt!")



# -------------------------
# 👨‍🏫 Trainer (≥3)
# -------------------------
trainer_data = [
    (1, "Anna", "Schmidt", "Yoga"),
    (2, "Max", "Müller", "Fitness"),
    (3, "Lisa", "Keller", "Pilates")
]

cursor.executemany("INSERT INTO Trainer VALUES (?, ?, ?, ?);", trainer_data)

# -------------------------
# 🧑 Mitglieder (≥6)
# -------------------------
mitglied_data = [
    (1, "Tom", "Becker", "tom@example.com", "2024-01-10"),
    (2, "Laura", "Fischer", "laura@example.com", "2024-02-15"),
    (3, "Jan", "Weber", "jan@example.com", "2024-03-20"),
    (4, "Sophie", "Wagner", "sophie@example.com", "2024-04-05"),
    (5, "Leon", "Hoffmann", "leon@example.com", "2024-05-01"),
    (6, "Emma", "Krüger", "emma@example.com", "2024-06-12")
]

cursor.executemany("INSERT INTO Mitglied VALUES (?, ?, ?, ?, ?);", mitglied_data)

# -------------------------
# 🏋️ Kurse (≥5)
# -------------------------
kurs_data = [
    (1, "Yoga Anfänger", "Montag", "18:00", 15, 1),
    (2, "Power Fitness", "Dienstag", "19:00", 20, 2),
    (3, "Pilates Basic", "Mittwoch", "17:00", 12, 3),
    (4, "Yoga Fortgeschritten", "Donnerstag", "18:30", 10, 1),
    (5, "HIIT Training", "Freitag", "20:00", 18, 2)
]

cursor.executemany("INSERT INTO Kurs VALUES (?, ?, ?, ?, ?, ?);", kurs_data)

# -------------------------
# 📝 Anmeldungen (≥8)
# -------------------------
anmeldung_data = [
    (1, 1, 1, "2024-07-01"),
    (2, 2, 1, "2024-07-02"),
    (3, 3, 2, "2024-07-02"),
    (4, 4, 3, "2024-07-03"),
    (5, 5, 4, "2024-07-03"),
    (6, 6, 5, "2024-07-04"),
    (7, 1, 2, "2024-07-05"),
    (8, 2, 3, "2024-07-06")
]

cursor.executemany("INSERT INTO Anmeldung VALUES (?, ?, ?, ?);", anmeldung_data)

conn.commit()
conn.close()

print("✅ Datenbank inkl. Beispieldaten erfolgreich erstellt!")