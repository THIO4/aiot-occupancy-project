# AIoT & ROBO LAB - Kävijäseuranta ja Ennustejärjestelmä

Tämä projekti on reaaliaikainen IoT-järjestelmä, joka seuraa laboratorion kävijämääriä MQTT-protokollan avulla, tallentaa datan SQLite-tietokantaan ja visualisoi sen ennustemallilla varustetulla Dashboardilla.

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
    ```bash
    python3 -m venv venv

**Virtuaaliympäristön aktivointi:**
    ```bash
    source venv/bin/activates

1. **Kloonaa repo:**
   ```bash
   git clone https://github.com/THIO4/aiot-occupancy-project
   cd projektin-kansio

2. **Asenna riippuvuudet:**
    ```bash
    pip install -r requirements.txt

3. **Käynnistä datankeruu taustalle**
    ```bash
    python src/mqtt_collector.py

**HUOM** 
**Sinun täytyy lisätä .env tiedosto projektin juurikansioon, josta mqtt_collector.py hakee sinun MQTT credentials seuraavassa muodossa:**
    ```bash
    MQTT_USER=********
    MQTT_PASS=********
    MQTT_HOST= ********
    MQTT_PORT=********
    MQTT_TOPIC=********


4. **Käynnistä dashboard**
    ```bash
    streamlit run src/dashboard.py

**MALLIN TULKINTA**
- **Harmaa katkoviiva: Historiallinen keskiarvo**
- **Turkoosi viiva: Tämän päivän toteuma**
- **Lämpökartta: Paljastaa ruuhkaisimmat viikonpäivät ja kellonajat**

