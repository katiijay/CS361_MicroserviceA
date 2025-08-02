Code for Microservice A (teammate)

How to request data from this Microservice: 
This microservice is accessible via an HTTP GET request to the endpoint: https://katiijay.pythonanywhere.com/forecast 
You can utilize a GET method to retrive the results with the following required parameters: 
lat=(numeric value between -90 and 90)
long=(numeric value between -180 and 180)
date=(date formatted as YYYYMMDD)

example of these params in the proper format: https://katiijay.pythonanywhere.com/forecast?lat=47.67043968751403&long=-122.5422167015877&date=20250802

How to receive data from this Microservice: 
This service returns a JSON-formatted set of results with high-level groupings for different weather attributes (temperature, cloud cover, etc.) and nested JSON elements for the daily statistics of these attributes and definition values. 
You can utilize any specific coding language of your choice to parse the information from this JSON tree. 
{
    "cloud": {
        "avg": 52.21,
        "max": 100,
        "min": 6,
        "scale": "%"
    },
    "precipitation": {
        "avg": 0.0,
        "max": 0.0,
        "min": 0.0,
        "scale": "inch"
    },
    "rainfall": {
        "avg": 0.0,
        "max": 0.0,
        "min": 0.0,
        "scale": "inch"
    },
    "snowfall": {
        "avg": 0.0,
        "max": 0.0,
        "min": 0.0,
        "scale": "inch"
    },
    "temperature": {
        "avg": 63.17,
        "max": 72.1,
        "min": 56.7,
        "scale": "\u00b0F"
    },
    "weather_code": {
        "scale": "WMO-CODE",
        "weather_code": 3,
        "weather_code_name": "overcast"
    },
    "wind": {
        "scale": "mp/h",
        "speed": 7.1
    }
}


README in screenshot(s) has UML sequence diagram that clearly communicates how to request and receive data from the microservice you implemented; No obvious notational errors

4.a. Alex Pettigrew

4.b. This microservice is fully operational and is live, hosted on PythonAnywhere domain. 

4.c. There is not currently rules to handle latitude and longitude values which are outside of range. These will currently throw a 500 error if you input out of range lat/long values. Revisions to have this return a 400 with appropriate error messaging will be in place by 8/5/2025

4.d. You can acess the microservice via an http call to https://katiijay.pythonanywhere.com/forecast. Access to this endpoint has required parameters; an example of a valid call is: https://katiijay.pythonanywhere.com/forecast?lat=47.67043968751403&long=-122.5422167015877&date=20250802
Github repository storing the code for this microservice is available here: https://github.com/katiijay/CS361_MicroserviceA 

4.e. If you cannot access the microservice, reach out to me with the error you're receiving via Teams. I'll respond within 24 hours per the rules we set in team communication guidelines. 

4.f. If you have issues with the microservice, please reach out sooner than 48 hours prior to the deadline that this microservice is blocking, that way I will have an opportunity to fix the issue and you can test it. For the end of course milestones, please reach out on or before 08/09/2025. 

4.g. N/A

