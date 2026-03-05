import sqlite3
import os

# Haetaan tämän tiedoston sijainti
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Rakennetaan polku: mennään yksi taso ylös (projektin juuri) ja sitten data-kansioon
DB_PATH = os.path.join(os.path.dirname(BASE_DIR), "data", "occupancy.db")

def get_connection():
    # Varmistetaan, että data-kansio on olemassa ennen yhdistämistä
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)



def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS occupancy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            device_id TEXT,        -- UUSI: vastaa JSONin "id"-kenttää
            topic TEXT NOT NULL,
            occupancy INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_record(timestamp, device_id, topic, occupancy):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO occupancy (timestamp, device_id, topic, occupancy)
        VALUES (?, ?, ?, ?)
    """, (timestamp, device_id, topic, occupancy))
    conn.commit()
    conn.close()