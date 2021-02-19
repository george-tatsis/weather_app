from marshmallow import Schema, fields, post_dump

class CitiesSchema(Schema):

	class Meta:
		ordered = True

	id = fields.Int(dump_only=True)
	title = fields.String(required=True)
	location_type = fields.String(required=True)
	woeid = fields.Integer(required=True)
	latt_long = fields.String(required=True)

	@post_dump(pass_many=True)
	def wrap(self,data,many,**kwargs):
		if many:
			return {'data':data}

		return data