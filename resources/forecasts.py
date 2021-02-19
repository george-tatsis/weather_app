from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.forecasts import Forecasts
from models.cities import Cities

from schemas.cities import CitiesSchema
from schemas.forecasts import ForecastsSchema

from config import URL_forecast, week

from webargs import fields
from webargs.flaskparser import use_kwargs

import datetime 

import requests

import os

city_schema = CitiesSchema()
forecasts_schema = ForecastsSchema(many=True,exclude=('id',))
forecasts_schema_user_id = ForecastsSchema(many=True,only=('location',))

class LatestForecastEachDay(Resource):

    def get(self,location):

        data = Cities.get_city_by_name(title=location)
        data = city_schema.dump(data).data

        city = Cities(**data)
        dates = Forecasts.get_location_date(city_id=city.id)
        dates = forecasts_schema.dump(dates).data

        return dates,HTTPStatus.OK


class MeanThreeLatestTemps(Resource):

    def get(self,location):

        data = Cities.get_city_by_name(title=location)
        data = city_schema.dump(data).data

        city = Cities(**data)
        dates = Forecasts.mean_temp_of_top_n(city_id=city.id,rank=3)
        dates = forecasts_schema.dump(dates).data

        return dates,HTTPStatus.OK


class TopNLocations(Resource):

    @use_kwargs({'topn': fields.Int(missing=3)})
    def get(self,metric,topn):
        dates = Forecasts.top_n_by_metric(metric=metric,topn=topn)
        dates = forecasts_schema.dump(dates).data

        return dates,HTTPStatus.OK

