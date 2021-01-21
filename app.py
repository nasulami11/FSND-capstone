import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS

from models import setup_db, db_drop_and_create_all, Actors, Movies, ActorMoviesMap
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # db_drop_and_create_all()

    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def index():
      return 'ji'

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def getAcotrs(jwt):

      actors = Actors.query.all()
      data =[]
  
      for actor in actors:
        moviesList = []
        movies = ActorMoviesMap.query.filter_by(Actor_id=actor.id).join(Movies).all()
        for movie in movies:
          moviesList.append({
            'title': movie.Movies.title
          })

        data.append({
          'Name': actor.name,
          'Age': actor.age,
          'Gender': actor.gender,
          'moviesList': moviesList
          })

      return jsonify({
                      'actors': data
                      })

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def getMovies(jwt):

      movies = Movies.query.all()
      data = []

      for movie in movies:
        actorsList = []
        actors = ActorMoviesMap.query.filter_by(Movie_id=movie.id).join(Actors).all()
        for actor in actors:
          actorsList.append({
            'name': actor.Actors.name
          })

        data.append({
          'title': movie.title,
          'relaseDate': movie.relaseDate,
          'actorsList': actorsList
          })

      return jsonify({
                      'actors': data
                      })

    @app.route('/actor', methods=['POST'])
    @requires_auth('post:actors')
    def addActor(jwt):
      parser = request.get_json()
      newName = parser['Name']
      newAge = parser['Age']
      newGender = parser['Gender']

      newActor = Actors(name=newName, age=newAge, gender=newGender)
      newActor.insert()

      return jsonify({
        'Success': True
      })

    @app.route('/movie', methods=['POST'])
    @requires_auth('post:movies')
    def addMovie(jwt):
      parser = request.get_json()
      newTitle = parser['title']
      newRelaseDate = parser['relaseDate']
      # newActors = json.dumps(parser['actors'])
      # print(newActors)

      newMovie = Movies(title=newTitle, relaseDate=newRelaseDate)
      newMovie.insert()

      return jsonify({
        'Success': True
      })

    @app.route('/actor/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def updateActor(jwt, actor_id):
      parser = request.get_json()

      if 'Name' not in parser and 'Age' not in parser and 'Gender' not in parser:
        abort(422)

      actors = Actors.query.filter_by(id=actor_id).first()
      if actors is None:
        abort(404)

      if 'Name' in parser:
        actors.name = parser['Name']

      if 'Age' in parser:
        actors.age = parser['Age']

      if 'Gender' in parser:
        actors.gender = parser['Gender']

      actors.update()

      return jsonify({
        'Success': True
      })

    @app.route('/movie/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patchMovie(jwt, movie_id):
      parser = request.get_json()
      print(parser)
      if 'title' not in parser and 'relaseDate' not in parser:
        abort(422)

      movies = Movies.query.filter_by(id=movie_id).first()
      print(movies)

      if movies is None:
        abort(404)

      if 'title' in parser:
        movies.title = parser['title']

      if 'relaseDate' in parser:
        movies.relaseDate = parser['relaseDate']

      movies.update()

      return jsonify({
        'Success': True
      })

    @app.route('/actor/<actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def deleteActor(jwt, actor_id):
      actors = Actors.query.filter_by(id=actor_id).first()
      if actors is None:
        abort(404)

      maps = ActorMoviesMap.query.filter_by(Actor_id=actor_id).all()

      for map in maps:
        map.delete()

      actors.delete()

      return jsonify({
        'Success': True
      })

    @app.route('/movie/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def deleteMovie(jwt, movie_id):
      movies = Movies.query.filter_by(id=movie_id).first()
      if movies is None:
        abort(404)

      maps = ActorMoviesMap.query.filter_by(Movie_id=movie_id).all()
      for map in maps:
        map.delete()
      movies.delete()

      return jsonify({
        'Success': True
      })

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                  "success": False,
                  "error": 422,
                  "message": "unprocessable"
                  }), 422

    @app.errorhandler(404)
    def notFound(error):
        return jsonify({
          "success": False,
          "error": 404,
          "message": "resource Not Found"
          }), 404

    @app.errorhandler(500)
    def internalServerError(error):
        return jsonify({
                  "success": False,
                  "error": 500,
                  "message": "internal Server Error"
                  }), 500

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
                  "success": False,
                  "error": 401,
                  "message": "unauthorized"
                  }), 401

    @app.errorhandler(AuthError)
    def process_AuthError(error):
      response = jsonify(error.error)
      response.status_code = error.status_code
      return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

