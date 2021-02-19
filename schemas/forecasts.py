from marshmallow import Schema, fields, post_dump
from schemas.cities import CitiesSchema

class ForecastsSchema(Schema):

	class Meta:
		ordered = True

	id = fields.Int(dump_only=True)
	weather_state_name = fields.String(required=True)
	weather_state_abbr = fields.String(required=True)
	wind_direction_compass = fields.String(required=True)
	created = fields.DateTime(required=True)
	applicable_date = fields.Date()
	min_temp = fields.Float(required=True)
	max_temp = fields.Float(required=True)
	the_temp = fields.Float(required=True)
	wind_speed = fields.Float(required=True)
	wind_direction = fields.Float(required=True)
	air_pressure = fields.Float(required=True)
	humidity = fields.Float(required=True)
	visibility = fields.Float(allow_none=True)
	predictability = fields.Float(required=True)
	avg_temp = fields.Float(allow_none=True)
	location = fields.Nested(CitiesSchema, attribute='cities', dump_only=True, only=['title'])


	@post_dump(pass_many=True)
	def wrap(self,data,many,**kwargs):
		if many:
			return {'data':data}

		return data

