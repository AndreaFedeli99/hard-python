import json
import requests
import datetime

basic_meteo_API_URL = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m&hourly=apparent_temperature&start_date={}&end_date={}&timezone=Europe/Rome"
province_fn = "hard-python/Lesson5/data/province.json"
with open(province_fn) as f:
    province_json = json.load(f)

def get_meteo_response(pr_name, date):
    try:
        province_coordinates = province_json[pr_name]
        respone_json = requests.get(basic_meteo_API_URL.format(province_coordinates['lat'],province_coordinates['lon'], date, date)).json()
        return respone_json
    except:
        raise ValueError("Please insert a valid province name!")

def print_current_temperature(pr_name, meteo_info):
    values_index = int(datetime.datetime.now().date().strftime("%H"))
    temp = meteo_info['hourly']['temperature_2m'][values_index]
    app_temp = meteo_info['hourly']['apparent_temperature'][values_index]
    temp_unit = meteo_info['hourly_units']['temperature_2m']
    app_temp_unit = meteo_info['hourly_units']['apparent_temperature']
    print("At {} the temperature is {}{}, the apparent temperature is {}{}".format(pr_name, temp, temp_unit, app_temp, app_temp_unit))

current_date = datetime.datetime.now().date()

province_name = input("Insert an italian province name: ")
meteo_info = get_meteo_response(province_name, current_date)
print_current_temperature(province_name, meteo_info)