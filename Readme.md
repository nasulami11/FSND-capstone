Casting Agency
-----

## Introduction

is app for casting agency to be used be the casting assitant and casting dirctor and executive producer to add movies and actors 

## Motivation 

I created this project to demonstrate the the skills i've gained in FSND such as auth0 code bulid and code deployments 

## Getting Started 
1. install requirements by running 
```
pip install -r requirements.txt
```

2.Local Database Setup

Once you create the database, open your terminal, navigate to the root folder, and run:
```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
After running, don't forget modify 'SQLALCHEMY_DATABASE_URI' variable.

Local Testing

To test your local installation, run the following command from the root folder:
```
python3 test_app.py
```
If all tests pass, your local installation is set up correctly


# Auth Details 
URL to retrive access token
https://dev-s6boul1u.us.auth0.com/authorize?audience=CastingAgency&response_type=token&client_id=aHTOQ3S6bwR1FgISLefCzxbKoR0PtV4v&redirect_uri=http://localhost:5000/login-result


1. Casting agent: Can view actors and movies.

email address :testcastingassistant410000@gmail.com



2. Casting director: Can view, add, modify, or delete actors; can view and modify movies.
email address :testcastingdirctor41000@gmail.com

3. Executive producer: Can view, add, modify, or delete actors and movies.
email address:testcastingexc41000@gmail.com


password : Test123-

## Api's

URL : http://fsnd-capstone-proj01.herokuapp.com

GET '/actors'
to view Actors 


-- response : 

{
    "actors": [
        {
            "Age": 51,
            "Gender": "Male",
            "Name": "Tom",
            "moviesList": [
                {
                    "title": "terminal"
                }
            ]
        },
        {
            "Age": 45,
            "Gender": "Female",
            "Name": "jennifer",
            "moviesList": [
                {
                    "title": "bad bosess"
                }
            ]
        }
    ]
}

##############

GET '/movies'
to view Movies 


-- response : 

{
    "actors": [
        {
            "actorsList": [
                {
                    "name": "jennifer"
                }
            ],
            "relaseDate": "Thu, 21 Jan 2021 00:00:00 GMT",
            "title": "bad bosess"
        },
        {
            "actorsList": [
                {
                    "name": "Tom"
                }
            ],
            "relaseDate": "Thu, 21 Jan 2021 00:00:00 GMT",
            "title": "terminal"
        }
    ]
}


POST '/actor'
to add a new actor 

-- request:

{
    "Age": 12,
    "Gender": "male",
    "Name": "naser"
}

-- response :

{
    "Success": true
}


POST '/movie'
to add a new movie 

-- request:

{
    "relaseDate": "Mon, 11 Jan 2021 00:00:00 GMT",
    "title": " daykkk"
}

-- response :

{
    "Success": true
}


PATCH '/actor/{{actor_id}}'
update actor info 

-- request:

{
    "Age": 12,
    "Gender": "male",
    "Name": "naser"
}

-- response :

{
    "Success": true
}


PATCH '/movie/{{movie_id}}'
update actor info 

-- request:

{
    "relaseDate": "Mon, 11 Jan 2021 00:00:00 GMT",
    "title": " daykkddddk"
}
-- response :

{
    "Success": true
}

DELETE '/actor/{{actor_id}}'


-- response :

{
    "Success": true
}


DELETE '/movie/{{movie_id}}'


-- response :

{
    "Success": true
}



