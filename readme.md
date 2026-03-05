# AIoT & ROBO LAB - Kävijäseuranta ja ennustejärjestelmä

Tämä projekti on reaaliaikainen IoT-järjestelmä, joka seuraa laboratorion kävijämääriä MQTT-protokollan avulla, tallentaa datan SQLite-tietokantaan paikallisesti ja visualisoi sen ennustemallilla varustetulla dashboardilla.

## Ominaisuudet
- **Reaaliaikainen seuranta:** MQTT-pohjainen datankeruu sensoreilta.
- **Älykäs Ennustaminen:** Laskee historiallisen datan perusteella "tyypillisen päivän" profiilin (24h) ja vertaa sitä nykyhetkeen.
- **Kumulatiivinen laskenta:** Laskee päivän kokonaiskävijämäärän (saapumiset), ei vain hetkellistä täyttöastetta.
- **Interaktiivinen Dashboard:** Toteutettu Streamlitillä ja Plotlyllä. Sisältää 24h-seurantagraafin ja viikoittaisen käyttöasteen lämpökartan.

## Tekniikat
- **Kieli:** Python 3
- **Kirjastot:** Streamlit, Pandas, Plotly, Paho-MQTT, SQLite3
- **Protokolla:** MQTT (JSON-viestit)

## Asennus ja käyttö

**Virtuaaliympäristö:**
    python3 -m venv venv


**Virtuaaliympäristön aktivointi:**

**Aktivointi (Linus/Mac):**
    source venv/bin/activate

**Aktivointi (Windows):**
    .\venv\Scripts\activate
    

1. **Kloonaa repo:**
   ```bash
   git clone https://github.com/THIO4/aiot-occupancy-project
   cd aiot-occupancy-project

2. **Asenna riippuvuudet:**
    ```bash
    pip install -r requirements.txt

3. **Käynnistä datankeruu taustalle**

**Tämä luo samalla data/occupancy.db tietokantatiedoston, johon data tallentuu**
    ```bash
    python src/mqtt_collector.py

**HUOM!** Sinun täytyy lisätä `.env`-tiedosto projektin juurikansioon, josta `mqtt_collector.py` hakee MQTT-tunnuksesi seuraavassa muodossa:

```env
MQTT_USER=kayttajanimi
MQTT_PASS=salasana
MQTT_HOST=broker.osoite.com
MQTT_PORT=1883
MQTT_TOPIC=labra/occupancy
```

4. **Käynnistä dashboard**
    ```bash
    streamlit run src/dashboard.py

**MALLIN TULKINTA**
- **Harmaa katkoviiva: Historiallinen keskiarvo**
- **Turkoosi viiva: Tämän päivän toteuma**
- **Lämpökartta: Paljastaa ruuhkaisimmat viikonpäivät ja kellonajat**

