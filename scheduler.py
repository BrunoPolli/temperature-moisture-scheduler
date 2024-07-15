import schedule
import time, datetime
import requests, os, logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='functions.log', level=logging.INFO)
temperature = 0

def get_temperature():
    start = datetime.datetime.now()
    logger.info(f"Starting request at: {start.strftime("%c")}")
    
    param = {'latitude': os.environ["LAT"], 'longitude': os.environ["LONG"], 'current': 'temperature_2m'}
    url = 'https://api.open-meteo.com/v1/forecast'
    temperature = 0

    try:
        res = requests.get(url, params=param).json()

        if res:
            temperature = res['current']['temperature_2m']

    except Exception as err:
        logger.error(err)


    end = datetime.datetime.now()
    logger.info(f"Finishing request at: {end.strftime("%c")}")

    return temperature

def send_data(temperature):
    url = f"{os.environ["ESP_URL"]}/update"
    
    data = {
        "data": {
            "temperature": temperature
            }
        }            

    try:
        req = requests.post(url, json= data, timeout=60)
        if req.status_code == 200:
            logger.info("Data sent to ESP32")
        else:
            logger.info(req.status_code)

        req.close()
    except Exception as err:
        logger.error(err)

def job():
    temperature = get_temperature()
    logger.info(f"TEMPERATURE: {temperature}")
    send_data(temperature)

# schedule.every(10).seconds.do(job)
schedule.every().hour.at(":00").do(job)
schedule.every().hour.at(":30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

