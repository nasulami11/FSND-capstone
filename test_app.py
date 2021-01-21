import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from app import create_app

from models import setup_db , db_drop_and_create_all , Actors , Movies , ActorMoviesMap



class test(unittest.TestCase):
    """This class represents the casting agency test case"""
    print('x')
    def setUp(self):
        """Define test variables and initialize app."""
        self.castingAssistantToken = os.environ['castingAssistant']
        self.castingDirctorToken = os.environ['castingDirctor']
        self.executiveProducerToken = os.environ['executiveProducer']
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.newActor = {
            "Age": 12,
            "Gender": "male",
            "Name": "naser"
        }

        self.newMovie = {
            "relaseDate": "Mon, 11 Jan 2021 00:00:00 GMT",
            "title": " daykkk"
        }

        self.updatedActor = {
            "Age": 16
            }

        self.updatedActorFali ={
            "Ages":12
        }

        self.updatedMoive = {
            "title": "interstller"
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def testGetAcotrsSucces(self):
        """ Test get Actors success"""
        res = self.client().get('/actors' , headers={'Authorization': self.castingAssistantToken})
        self.assertEqual(res.status_code, 200)
    
    def testGetAcotrsFaliure(self):
        """ testGetAcotrsFaliure"""
        res = self.client().get('/actorr' , headers={'Authorization': self.castingAssistantToken})
        
        self.assertEqual(res.status_code, 404)

    def testGetMoviesSucces(self):
        """ testGetMoviesSucces"""
        res = self.client().get('/movies' , headers={'Authorization': self.castingAssistantToken})
        
        self.assertEqual(res.status_code, 200)
    
    def testGetMoviesFaliure(self):
        """ testGetMoviesFaliure"""
        res = self.client().get('/moivee' ,headers={'Authorization': self.castingAssistantToken})
        
        self.assertEqual(res.status_code, 404)

    def testPostActorsSuccess(self):
        """ testPostActorsSuccess"""
        res = self.client().post('/actor' ,headers={'Authorization': self.castingDirctorToken} , json=self.newActor)

        self.assertEqual(res.status_code, 200)

    def testPostActorsFaliure(self):
        """ testPostActorsFaliure"""
        res = self.client().get('/actor' , headers={'Authorization': self.castingDirctorToken} ,json=self.newActor )
        self.assertEqual(res.status_code, 405)

    def testPostMoviesSuccess(self):
        """ testPostMoviesSuccess"""
        res = self.client().post('/movie'  ,headers={'Authorization': self.executiveProducerToken},json=self.newMovie)

        self.assertEqual(res.status_code, 200)

    def testPostMoivesFaliure(self):
        """ testPostMoivesFaliure"""
        res = self.client().get('/movie' , headers={'Authorization': self.executiveProducerToken} , json=self.newMovie)
        self.assertEqual(res.status_code, 405)

    def testPatchActorsSuccess(self):
        """ testPatchActorsSuccess"""
        res = self.client().patch('/actor/4'  , headers={'Authorization': self.castingDirctorToken} , json=self.updatedActor)

        self.assertEqual(res.status_code, 200)

    def testPatchActorsFaliure(self):
        """ Test post Actors faliure"""
        res = self.client().patch('/actor/2'  , headers={'Authorization': self.castingDirctorToken} , json=self.updatedActorFali)
        self.assertEqual(res.status_code, 422)

    def testPatchMoviesSuccess(self):
        """ testPatchMoviesSuccess"""
        res = self.client().patch('/movie/3' , headers={'Authorization': self.castingDirctorToken} , json=self.updatedMoive )

        self.assertEqual(res.status_code, 200)

    def testPatchMoivesFaliure(self):
        """ testPatchMoivesFaliure"""
        res = self.client().patch('/movie/9997'  , headers={'Authorization': self.castingDirctorToken} , json=self.updatedMoive)
        self.assertEqual(res.status_code, 404)


    def testDeleteActorsSuccess(self):
        """ testDeleteActorsSuccess"""
        res = self.client().delete('/actor/1'  , headers={'Authorization': self.castingDirctorToken})

        self.assertEqual(res.status_code, 200)

    def testDeleteActorsFaliure(self):
        """ testDeleteActorsFaliure"""
        res = self.client().delete('/actor/9997'  ,headers={'Authorization': self.castingDirctorToken})
        self.assertEqual(res.status_code, 404)

    def testDeleteMoviesSuccess(self):
        """ testDeleteMoviesSuccess"""
        res = self.client().delete('/movie/1' ,headers={'Authorization': self.executiveProducerToken})
        self.assertEqual(res.status_code, 200)

    def testDeleteMoivesFaliure(self):
        """ testDeleteMoivesFaliure"""
        res = self.client().delete('/movie/9997' ,headers={'Authorization': self.executiveProducerToken})
        self.assertEqual(res.status_code, 404)


    def testCastingAssistantFail(self):
        """ Test patch Actors with casting assistant"""
        res = self.client().patch('/actor/2'  , headers={'Authorization': self.castingAssistantToken} , json=self.updatedActor)

        self.assertEqual(res.status_code, 403)

    def testCastingDirctorFail(self):
        """ Test delete movie with casting dirctor"""
        res = self.client().delete('/movie/2'  , headers={'Authorization': self.castingDirctorToken})

        self.assertEqual(res.status_code, 403)


    

    





    




if __name__ == "__main__":
    unittest.main()
