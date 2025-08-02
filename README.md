## Code for Microservice A (teammate)

### How to request data from this Microservice: 
This microservice is accessible via an HTTP GET request to the endpoint: https://katiijay.pythonanywhere.com/forecast 

You can utilize a GET method to retrive the results with the following required parameters: 

- lat=(numeric value between -90 and 90)
- long=(numeric value between -180 and 180)
   date=(date formatted as YYYYMMDD)
  
example of these params in the proper format: 
- https://katiijay.pythonanywhere.com/forecast?lat=47.67043968751403&long=-122.5422167015877&date=20250802

### How to receive data from this Microservice: 
This service returns a JSON-formatted set of results with high-level groupings for different weather attributes (temperature, cloud cover, etc.) and nested JSON elements for the daily statistics of these attributes and definition values. 

You can utilize any specific coding language of your choice to parse the information from this JSON tree. 

Example
```
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
```
### UML Sequence Diagram 
![UML Diagram of request and response flow](https://github.com/katiijay/CS361_MicroserviceA/blob/main/UML_Diagram.png?raw=true)
