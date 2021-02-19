from marshmallow import Schema, fields

class RequestSchema(Schema):

	class Meta:
		ordered = True

	location_1 = fields.String(required=True)
	location_2 = fields.String(required=True)
	location_3 = fields.String(required=True)