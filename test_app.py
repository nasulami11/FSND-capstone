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
        self.castingAssistantToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjlOcko2VS1VY3hUZy1jajYxcm1zSSJ9.eyJpc3MiOiJodHRwczovL2Rldi1zNmJvdWwxdS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwMzk3NzIxMzIzZWQwMDZhZmNlY2NhIiwiYXVkIjoiQ2FzdGluZ0FnZW5jeSIsImlhdCI6MTYxMTE4NTQ4NSwiZXhwIjoxNjExMjcxODg1LCJhenAiOiJhSFRPUTNTNmJ3UjFGZ0lTTGVmQ3p4YktvUjBQdFY0diIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.o6il8pXEBIyl9clAz5KGj83sCdR1Y_CbM6A6FrW-Yg2H_g9MtZjfqWP90eEwJxGaLYgIzFvzMO7Z1hZvuvYb0-_fAtmRJ-uMJ_nJCn5AJjzakqQuJ5D72ZUZPGGkvdc19x_JS36IiPZfRG7KvGLLZGL1dbaJ8X7KDLikUM_tQdV6bbOdm2E3KyWdquSu89jSxfI8f3gNk2ldcu2QpVMtxpIGfjDeqSGi8eElVgMQDOUafXnunpUwyj7PsuCmCD9q4ggxGRpp9zdJ5DNp_KAMAWN_rvDRDfaHBfYJYrkQXdqSraJeNxHbYBEkbGLTBByyazVJZQlPQ_1Bhahzc1LNAQ"
        self.castingDirctorToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjlOcko2VS1VY3hUZy1jajYxcm1zSSJ9.eyJpc3MiOiJodHRwczovL2Rldi1zNmJvdWwxdS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwMzk3ZDEzMjI1ZjkwMDc3Y2ZkZjU5IiwiYXVkIjoiQ2FzdGluZ0FnZW5jeSIsImlhdCI6MTYxMTE4NTU4MiwiZXhwIjoxNjExMjcxOTgyLCJhenAiOiJhSFRPUTNTNmJ3UjFGZ0lTTGVmQ3p4YktvUjBQdFY0diIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.kPdGZK3GUB19PBQgyqZEWzkWy-X-c-ambcG5M075R6u7YtkaAJ7YuwP5FYLEXcG3ma6q4-vsvDcrYU-nZEThC_BvmJoLP6iMxeQDjwIZq5wesgPepOoj6Y_ptY3nwr3VJ336g4NEeJXeOVSFK_SiGcMVEOXVV6mMmfbFghABgR-M-UBFWcIwrcTBZdmVKXUdFLqF7atzuxO68tSbkA2KVZpfmtWpE37tup2rOz_e8TYtPS4YFnGXaXFmtkULipHR_0hwakX9DKpKGHKca9vzNkjju01Oh2bthjoCw3n_Rxq0KXNSlu_sV0pL7SM8TJ5gY_cASToBj4owmieSPErxXg"
        self.executiveProducerToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjlOcko2VS1VY3hUZy1jajYxcm1zSSJ9.eyJpc3MiOiJodHRwczovL2Rldi1zNmJvdWwxdS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwMzk4MDYxNTIyMTgwMDZhM2M5ODA3IiwiYXVkIjoiQ2FzdGluZ0FnZW5jeSIsImlhdCI6MTYxMTE4NTM2NywiZXhwIjoxNjExMjcxNzY3LCJhenAiOiJhSFRPUTNTNmJ3UjFGZ0lTTGVmQ3p4YktvUjBQdFY0diIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.sk3q0vfTdr6clcYzKBQQsOYAjoqiU0VUff5NcT9g-zJFJRxmUrAkin6grNfG3swyqHwCwYKfwVZbLl3xDxGbiFmT76nSKI2hBJZLdh2lZRZo8DSHy0gouD39jL6G9iJYXeVBO5bFQyczO8t38uQldxu8ePzPZyC2lDivK0W28EMADX0kRnQT0-Ek-qchL6-AR6wGbFSvCCGO9NmPetNmr-K7TmyuuRxAahweTkUoaDrAdzhElclTeD9RpbEkQ3AEAf_YcQhwbC1fwm2oGe10ef671asahsys937GZGtE8HeNTtNuVqFS6AUol2IdU9lSWBEpJQbcvLtB4yWAn_hQvg"
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
