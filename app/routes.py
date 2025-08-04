from app import app
from flask import jsonify, request
from .calls.weathercall import get_weather
from urllib import error

@app.route('/forecast', methods=['GET'])
def get_forecast():
    latitude = request.args.get('lat')
    longitude = request.args.get('long')
    date = request.args.get('date')
    results = {}
    try:
        results = get_weather(latitude, longitude, date)
    except error.HTTPError as err:
        print(err.code)
        return err.code
    #if date < datetime.today():
    #    raise ValueError('Cannot retrieve a forecast for a day that has already occurred')
    return jsonify(results)