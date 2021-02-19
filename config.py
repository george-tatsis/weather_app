import datetime

URL_location = "https://www.metaweather.com/api/location/search/?query="
URL_forecast = "https://www.metaweather.com/api/location/" 

today = datetime.date.today()
week = [today - datetime.timedelta(days=i) for i in range(7)]

class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{username}:{password}@localhost:5432/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False