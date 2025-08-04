# Citation for weather codes, used the mappings from https://github.com/Leftium/weather-sense/blob/62d94b403f198c5531cf9e74f09d995249eb6a5a/src/lib/util.ts#L46

import requests
from datetime import datetime 
from datetime import timedelta


def get_request(url=str, params=dict):
    # handles request to API. 
    responses = requests.get(url=url, params=params)
    return responses.json()

def weather_code_helper(code=int):
    # determines friendly name of weather code.
    weather_code = 'unknown'
    if   code == 0:  weather_code = 'clear'
    elif code == 1:  weather_code = 'mostly-clear'
    elif code == 2:  weather_code = 'partly-cloudy'
    elif code == 3:  weather_code = 'overcast'
    elif code == 45: weather_code = 'fog'
    elif code == 48: weather_code = 'rime-fog'
    elif code == 51: weather_code = 'light-drizzle'
    elif code == 53: weather_code = 'moderate-drizzle'
    elif code == 55: weather_code = 'dense-drizzle'
    elif code == 56: weather_code = 'light-freezing-drizzle'
    elif code == 57: weather_code = 'dense-freezing-drizzle'
    elif code == 66: weather_code = 'light-freezing-rain'
    elif code == 67: weather_code = 'heavy-freezing-rain'
    elif code == 73: weather_code = 'moderate-snowfall'
    elif code == 77: weather_code = 'snowflakes'
    elif code == 95: weather_code = 'thunderstorm'
    elif code == 80 or code == 61: weather_code = 'light-rain'
    elif code == 81 or code == 63: weather_code = 'moderate-rain'
    elif code == 82 or code == 65: weather_code = 'heavy-rain'
    elif code == 71 or code == 85: weather_code = 'slight-snowfall'
    elif code == 86 or code == 75: weather_code = 'heavy-snowfall'
    elif code == 96 or code == 99: weather_code = 'thunderstorm-with-hail'

    return weather_code


def statistics_builder(results=dict, param=str):
    # builds out the statistical values and scale for using across different forecast measures. 
    header_name = 'hourly_units'
    value_name = 'hourly'
    results_vals = results[value_name][param]
    results_scale = results[header_name][param]
    print(results_scale)
    val_list = []
    val_sums = 0
    for val in results_vals:
        val_list.append(val)
        val_sums += int(val)
    val_max = max(val_list)
    val_min = min(val_list)
    val_avg = val_sums/len(val_list)
    return[val_max, val_min, val_avg, results_scale]


def get_weather(lat=float, long=float, date=str):
    # sets parameters for API request and assembles results into appropriate statistics for project. 
    url = 'https://api.open-meteo.com/v1/forecast'
    date_converted = f'{date[0:4]}-{date[4:6]}-{date[6:8]}'
    max_date = (datetime.today() + timedelta(days=14)).date()
    if datetime.strptime(date_converted, '%Y-%m-%d').date() > max_date:
        return f"Date is too far in the future to be forecasted, please request a date on or before {max_date}", 400
    if float(lat) < -90 or float(lat) > 90:
        return "Inappropriate range for Latitude", 400
    if float(long) < -180 or float(long) > 180:
        return "Inappropriate range for Longitude", 400
    
    params = {
        'latitude': lat,
        'longitude': long,
        "timezone": "auto",
        'hourly': ['temperature_2m', 'precipitation', 'cloud_cover', 'weather_code', 'wind_speed_10m', 'rain', 'snowfall'],
        'wind_speed_unit': 'mph',
        'temperature_unit': 'fahrenheit',
        'precipitation_unit': 'inch',
        'start_date': date_converted,
        'end_date': date_converted,
    }
    weather_results = get_request(url=url, params=params)
    results = {}

    # finding max wind_speed and putting into results
    wind_results = statistics_builder(weather_results, 'wind_speed_10m')
    dict_vals = {'speed':wind_results[0], 'scale':wind_results[3]}
    results['wind'] = dict_vals

    # finding min and max temperatures and putting into results
    temp_results = statistics_builder(weather_results, 'temperature_2m')
    dict_vals =  {'max': temp_results[0], 'min':temp_results[1], 'avg':temp_results[2], 'scale':temp_results[3]}
    results['temperature'] = dict_vals

    # finding cloud coverage and putting into the results
    cloud_results = statistics_builder(weather_results, 'cloud_cover')
    dict_vals =  {'max':cloud_results[0], 'min':cloud_results[1], 'avg':cloud_results[2], 'scale':cloud_results[3]}
    results['cloud'] = dict_vals

    # finding precipitation and putting into the results
    prec_results = statistics_builder(weather_results, 'precipitation')
    dict_vals =  {'max':prec_results[0], 'min':prec_results[1], 'avg':prec_results[2], 'scale':prec_results[3]}
    results['precipitation'] = dict_vals

    # finding precipitation and putting into the results
    snow_results = statistics_builder(weather_results, 'snowfall')
    dict_vals =  {'max':snow_results[0], 'min':snow_results[1], 'avg':snow_results[2], 'scale':snow_results[3]}
    results['snowfall'] = dict_vals

    # finding precipitation and putting into the results
    rain_results = statistics_builder(weather_results, 'rain')
    dict_vals =  {'max':rain_results[0], 'min':rain_results[1], 'avg':rain_results[2], 'scale':rain_results[3]}
    results['rainfall'] = dict_vals

    # finding most frequent weather code for reporting weather "type"
    weather_vals = weather_results['hourly']['weather_code']
    val_list = []
    for val in weather_vals:
        val_list.append(val)
    weather_code_daily = max(set(val_list), key = val_list.count)
    weather_code = weather_code_helper(weather_code_daily)

    dict_vals =  {'weather_code': weather_code_daily, 'weather_code_name': weather_code, 'scale':'WMO-CODE'}
    results['weather_code'] = dict_vals

    return results
