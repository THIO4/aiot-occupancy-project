import pandas as pd
import sqlite3
import os

def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(os.path.dirname(BASE_DIR), "data", "occupancy.db")
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM occupancy", conn, parse_dates=['timestamp'])
    conn.close()
    return df

def get_24h_profile(df):
    if df.empty:
        return pd.DataFrame(columns=['hour', 'predicted_occupancy'])
    
    df = df.copy()
    df['hour'] = df['timestamp'].dt.hour
    
    # Lasketaan keskiarvo ja pyöristetään kokonaisluvuksi
    profile = df.groupby('hour')['occupancy'].mean().round(0).astype(int).reset_index()
    profile.rename(columns={'occupancy': 'predicted_occupancy'}, inplace=True)
    
    all_hours = pd.DataFrame({'hour': range(24)})
    profile = pd.merge(all_hours, profile, on='hour', how='left').fillna(0)
    return profile

def get_weekly_heatmap_data(df):
    if df.empty:
        return pd.DataFrame()

    df = df.copy()
    df['hour'] = df['timestamp'].dt.hour
    df['day_name'] = df['timestamp'].dt.day_name()
    
    # Käytetään max() keskiarvon sijaan, jotta piikit näkyvät paremmin.
    # Pyöristetään ja nimetään sarake valmiiksi.
    heatmap_data = df.groupby(['day_name', 'hour'])['occupancy'].max().round(0).astype(int).reset_index()
    heatmap_data.rename(columns={'occupancy': 'predicted_occupancy'}, inplace=True)
    
    suomi_paivat = {
        'Monday': 'Ma', 'Tuesday': 'Ti', 'Wednesday': 'Ke', 
        'Thursday': 'To', 'Friday': 'Pe', 'Saturday': 'La', 'Sunday': 'Su'
    }
    heatmap_data['day_name'] = heatmap_data['day_name'].map(suomi_paivat)
    return heatmap_data