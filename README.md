# Temperature/Moisture scheduler

This scheduler script is responsible for two tasks: send data to update TFT display, and retrieve data in NodeMCU ESP8266 12v-e server.

Temperature value is obtained by Open Meteo API: https://open-meteo.com/, and sent to NodeMCU server. This request is processed by NodeMCU and shown in TFT display.

## Installation
Python 3.12.0

Virtual Environment
- python -m venv venv
- .\venv\Scripts\activate
- pip install -r requirements.txt

Starting scheduler
- python .\scheduler.py

## Display project
https://github.com/BrunoPolli/display-temperature-moisture
