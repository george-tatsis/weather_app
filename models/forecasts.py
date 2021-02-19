from extensions import db
from sqlalchemy.sql import func
from sqlalchemy import text


class Forecasts(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, primary_key=True)
    weather_state_name = db.Column(db.String(100))
    weather_state_abbr = db.Column(db.String(100))
    wind_direction_compass = db.Column(db.String(100))
    created = db.Column(db.DateTime(200))
    applicable_date = db.Column(db.Date())
    min_temp = db.Column(db.Float())
    max_temp = db.Column(db.Float())
    the_temp = db.Column(db.Float())
    wind_speed = db.Column(db.Float())
    wind_direction = db.Column(db.Float())
    air_pressure = db.Column(db.Float())
    humidity = db.Column(db.Float())
    visibility = db.Column(db.Float(),default=None)
    predictability = db.Column(db.Float())

    city_id = db.Column(db.Integer(),db.ForeignKey("cities.id"))


    @classmethod
    def get_by_location(cls,city_id):
        return cls.query.filter_by(city_id=city_id).first()

    @classmethod
    def get_location_date(cls,city_id,):

        subquery = db.session.query(cls,func.rank().over(
                                    order_by=cls.created.desc(),
                                    partition_by=cls.applicable_date
                                        ).label('rnk')
                                    ).filter_by(city_id=city_id).subquery()


        return db.session.query(subquery).filter(subquery.c.rnk==1).all()

    @classmethod
    def mean_temp_of_top_n(cls,city_id,rank):
        subquery = db.session.query(cls,func.rank().over(
                                    order_by=cls.created.desc(),
                                    partition_by=cls.applicable_date
                                        ).label('rnk')
                                    ).filter_by(city_id=city_id).subquery()

        subquery = db.session.query(subquery).filter(subquery.c.rnk<=rank).subquery()
        
        return db.session.query(subquery.c.applicable_date,func.avg(subquery.c.the_temp).label('avg_temp')).group_by(subquery.c.applicable_date).all()

    @classmethod
    def top_n_by_metric(cls,metric,topn):

        return cls.query.order_by(text("{} desc".format(metric))).limit(topn)


    def save(self):
        db.session.add(self)
        db.session.commit()