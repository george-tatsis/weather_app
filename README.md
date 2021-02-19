# Weather API

## Descritpion

An app with which you get the forecasts of any three locations and for a period of 7 days.
we will use the https://www.metaweather.com/api/ api.

A forecast is of the following form

```
{

    "weather_state_name": sting,
    "weather_state_abbr": sting,
    "wind_direction_compass": sting,
    "created": sting,
    "applicable_date": sting,
    "min_temp": float,
    "max_temp": float,
    "the_temp": float,
    "wind_speed": float,
    "wind_direction": float,
    "air_pressure": float,
    "humidity": float,
    "visibility": float,
    "predictability": float

}
```

## How to run it

First installing dependecies 

`~$ pip install -r requierements.txt`

Modify the username, password and database name in the config.py file and then initializing and migrating and updating the database

`~$ flask db init`

`~$ flask db migrate`

`~$ flask db upgrade`

Then initialize the app:

`~$ python app.py` 

while being in the weather_app folder

## Usage

### Viewing the documentation

**Definition**

`Get /`

**Response**

Present some documentation

### Requesting weather data for 3 locations 

**Definiton**

`POST /request`

**Argument**

- `"location_1": string` location name
- `"location_2": string` location name
- `"location_3": string` location name 


pass the argument in json format


```json
{
    "location_1": "athens",
    "location_2": "london",
    "location_3": "san francisco"
}
```

## Queries

For each Get request for a query a csv will be created with the extracted data in the Queries folder.

### List all locations

**Definition**

`Get /request/locations`

**Response**

- `200 OK` on success



```list
["Athens","London","San Francisco"]
```

### List the latest forecast for each location for every day

**Definiton**

`Get /request/locations/<string:location>/latest`

**Response**

- `200 OK` on success

```list [

        {forecast_1},
        {forecast_2},
        {forecast_3},
        {forecast_4},
        {forecast_5},
        {forecast_6},
        {forecast_7}

        ]
```

### List the average the_temp of the last 3 forecasts for each location for every day

**Definiton**

`Get /request/locations/<string:location>/mean`

**Response**

- `200 OK` on success

```list [

        {"applicable_date":<date>,"avg_temp":<average_temp>},
        {"applicable_date":<date>,"avg_temp":<average_temp>},
        {"applicable_date":<date>,"avg_temp":<average_temp>},
        
        ...],

```

### Get the top n forecasts along iwth the location based on a specific metric.

**Definiion**

`Get /request/locations/<string:metric>?<integer:topn>`

(default topn=3)

**Response**

- `200 OK` on success

```json{
    "data" : [

                {
                "weather_state_name": sting,
                "weather_state_abbr": sting,
                "wind_direction_compass": sting,
                "created": sting,
                "applicable_date": sting,
                "min_temp": float,
                "max_temp": float,
                "the_temp": float,
                "wind_speed": float,
                "wind_direction": float,
                "air_pressure": float,
                "humidity": float,
                "visibility": float,
                "predictability": float,
                "location":{
                    "title":string
                            }
                },

                {
                "weather_state_name": sting,
                "weather_state_abbr": sting,
                "wind_direction_compass": sting,
                "created": sting,
                "applicable_date": sting,
                "min_temp": float,
                "max_temp": float,
                "the_temp": float,
                "wind_speed": float,
                "wind_direction": float,
                "air_pressure": float,
                "humidity": float,
                "visibility": float,
                "predictability": float,
                "location":{
                    "title":string
                            }
                },
                ...
            ]
}
```