import os

import markdown

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db

from resources.cities import ApiRequestCities, CitiesListResource 
from resources.forecasts import LatestForecastEachDay, MeanThreeLatestTemps, TopNLocations

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	register_extensions(app)
	register_resources(app)

	@app.route("/")
	def index():
		"""Present some documentation"""

		#Open the README file
		with open("README.md", 'r') as markdown_file:

			# Read the content of the file
			content = markdown_file.read()


			# Convert to HTML
			return markdown.markdown(content)


	return app


def register_extensions(app):
	db.app = app
	db.init_app(app)
	migrate = Migrate(app,db)


def register_resources(app):
	api = Api(app)

	api.add_resource(ApiRequestCities,'/request')
	api.add_resource(CitiesListResource,'/request/locations')
	api.add_resource(LatestForecastEachDay,'/request/locations/<string:location>/latest')
	api.add_resource(MeanThreeLatestTemps,'/request/locations/<string:location>/mean')
	api.add_resource(TopNLocations,'/request/locations/<string:metric>')


if __name__=="__main__":
	app = create_app()
	app.app_context().push()
	app.run()