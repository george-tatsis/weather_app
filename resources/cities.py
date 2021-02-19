from flask import request
from flask_restful import Resource
from http import HTTPStatus

from config import Config, URL_location, URL_forecast, week

from models.cities import Cities
from models.forecasts import Forecasts

from schemas.cities import CitiesSchema
from schemas.api_request import RequestSchema
from schemas.forecasts import ForecastsSchema

import datetime 

import requests

import os

city_schema = CitiesSchema()
city_title_schema = CitiesSchema(only=('title',),many=True)
request_schema = RequestSchema()
forecasts_schema = ForecastsSchema()


class ApiRequestCities(Resource):
	def post(self):
		json_data = request.get_json()

		data, errors = request_schema.load(data=json_data)
		if errors:
			return {'message':'Validation errors', 'errors':errors},HTTPStatus.BAD_REQUEST

		Forecasts.query.delete()
		Cities.query.delete()

		for city in json_data.values():
			

			PARAMS = {"query":city} 
			r = requests.get(url = URL_location, params = PARAMS)
			json_data = r.json()[0]

			data, errors = city_schema.load(data=json_data)
			if errors:
				return {'message':'Validation errors', 'errors':errors},HTTPStatus.BAD_REQUEST

			city = Cities(**data)	
			city.save()    
	            
			for day in week:

				date = day.strftime("%Y/%m/%d")
				URL = os.path.join(URL_forecast,str(city.woeid),date)
				api_req = requests.get(url = URL) 
				data_week = api_req.json()

				for json_data in data_week:

					try :
						del json_data['id']
					except:
						pass

					data, errors = forecasts_schema.load(data=json_data)

					if errors:
						return {'message':'Validation errors', 'errors':errors},HTTPStatus.BAD_REQUEST

					forecast = Forecasts(**data)  
					forecast.city_id = city.id
					forecast.save() 

		return {},HTTPStatus.NO_CONTENT


class CitiesListResource(Resource):

	def get(self):

		cities = Cities.get_all_cities()
		cities = city_title_schema.dump(cities).data.get('data')

		return [city.get('title') for city in cities], HTTPStatus.OK

