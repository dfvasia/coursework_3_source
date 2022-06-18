from project.config import DevelopmentConfig
from project.dao.models import Genre, Director, User, Movie
from project.server import create_app, db


app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
	try:
		return {
			"db": db,
			"Genre": Genre,
			"Director": Director,
			"User": User,
			"Movie": Movie
		}
	except ImportError as e:
		print(e)

