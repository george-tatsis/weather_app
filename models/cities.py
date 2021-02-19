from extensions import db


class Cities(db.Model):

	__tablename__ = 'cities'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20),nullable=False)
	location_type = db.Column(db.String(50),nullable=False)
	woeid = db.Column(db.Integer,nullable=False)
	latt_long = db.Column(db.String(50),nullable=False)

	forecastes = db.relationship('Forecasts', backref='cities')

	@classmethod
	def get_all_cities(cls):
	    return cls.query.all()

	@classmethod
	def get_city_by_name(cls,title):
		return cls.query.filter_by(title=title).first()


	def save(self):
	    db.session.add(self)
	    db.session.commit()
