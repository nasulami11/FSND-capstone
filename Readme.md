Casting Agency
-----

## Introduction

is app for casting agency to be used be the casting assitant and casting dirctor and executive producer to add movies and actors 

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


# Auth Details 
URL to retrive access token
https://dev-s6boul1u.us.auth0.com/authorize?audience=CastingAgency&response_type=token&client_id=aHTOQ3S6bwR1FgISLefCzxbKoR0PtV4v&redirect_uri=http://localhost:5000/login-result



casting assistant email address :testcastingassistant410000@gmail.com
casting dirctor  email address :testcastingdirctor41000@gmail.com
executive producer  email address:testcastingexc41000@gmail.com

password : Test123-

