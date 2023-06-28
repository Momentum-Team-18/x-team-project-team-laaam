# Team LAAM BE README

**Token Authentication System**
* Djoser
* Docs: https://djoser.readthedocs.io/en/latest/introduction.html
  
**Deployment**
* Render
* Main Webservice Address: https://cards-q6a8.onrender.com
* Database: Postgresql@14
* Docs: https://render.com/docs/deploy-django

**Endpoints**
|Method  |URL                         |Input                             |Output                                   |Notes                                         |
|--------|----------------------------|----------------------------------|-----------------------------------------|----------------------------------------------|
|LOGIN   |auth/token/login/           |{{User.USERNAME_FIELD}}, password |HTTP_200_OK, auth_token|token create     |                                              |
|LOGOUT  |auth/token/logout/          |-                                 |HTTP_204_NO_CONTENT                      |                                              |
|        |                            |                                  |                                         |                                              |
|GET     |api/cards/                  |                                  |list of all cards                        |
|POST    |api/cards/                  |card data                         |new card                                 |retrieves card detail with specified pk       |
|PATCH   |api/cards/<int:pk>/         |card data                         |updated card                             |updates card with specified pk                |
|DELETE  |api/cards/<int:pk>/         |-                                 |-                                        |deletes card with specified pk                | 
|GET     |api/profile/<int:pk>        |-                                 |user info                                |retrieves user with specified pk profile info |
|PATCH   |api/profile/<int:pk>/       |-                                 |updated user profile                     |updates user profile with specified pk        |
|DELETE  |api/profile/<int:pk>/       |-                                 |-                                        |deletes user profile with specified pk        |
|GET     |api/cards/sent/             |-                                 |list of cards logged in user has sent    |associated field: sent_by_user, read-only     |
|GET     |api/cards/received/         |-                                 |list of cards logged in user has received|associated field: sent_to_user, read-only     |
|GET     |api/user_following/         |                                  |list of followers user is following      |
|GET     |api/user_followers/         |                                  |list of followers of user                |
|POST    |api/follow_user/            |username of user to be followed   |new follow relatioship                   |relationship is btw signed-in user and user they've requested to follow|
|DELETE  |api/unfollow_user/<int:pk>  |-                                 |-                                        |<int:pk> is the follow relationship id (not user id/pk)|



**Create User**

**request**
> POST  auth/users/
> {
> "username": "superuser",
> "password": "somepassword"
> }

**response**
> HTTP_201_created
> {
> "username": "superuser",
> "password": "somepassword",
> "id": 1
> }


**LOGIN**

**request**
> POST auth/token/login/
> {
> "username": "superuser",
> "password": "somepassword"
> }

**response**
> HTTP_200_OK
> {
> "auth_token": "somereallylonglistofnumbersandletters"
> }


**LOGOUT**

**requests**
> POST auth/token/logout/

**response**
> HTTP_204_NO_CONTENT


**PROFILE**

**requests**
> GET api/profile/<username>/

**response**
> {
>	"username": "superuser",
>	"first_name": "",
>	"last_name": "",
>	"bio": null,
>	"date_joined": "2023-06-26T23:45:36.884115Z",
>	"cards_sent": [
>		  {
>			"id": 12,
>			"sent_by_user": "superuser",
>			"sent_to_user": "mouse",
>			"image_urls": null,
>			"date_created": "2023-06-27T12:14:01.348168Z",
>			"privacy": true,
>			"headline": "Hello!",
>			"front_text": "I miss you.",
>			"inner_text": "Love, Mouse",
>			"likes": 15,
>			"background_color": "Blue",
>			"border_color": "Red",
>			"border_decor": "Solid",
>			"font_color": "Black",
>			"header_font": "Script",
>			"front_text_font": "Script",
>			"back_text_font": "Script"
>		 },
>  ],
>	"cards_received": [
>		  {
>			"id": 11,,
>			"sent_by_user": "mouse",
>			"sent_to_user": "superuser",
>			"image_urls": null,
>			"date_created": "2023-06-28T12:14:30.737243Z",
>			"privacy": true,
>			"headline": "Happy Holidays",
>			"front_text": "From our family to yours",
>			"inner_text": "Love, Mr & Mr Mouse",
>			"likes": 150,
>			"background_color": "Blue",
>			"border_color": "Blue",
>			"border_decor": "Dotted",
>			"font_color": "Yellow",
>			"header_font": "Script",
>			"front_text_font": "Script",
>			"back_text_font": "Script"
>		 },
]

**request**
> PATCH  api/profile/<username>/

**response**
> Changes made to profile:
>    {
>			"id": 11,,
>			"sent_by_user": "mouse",
>			"sent_to_user": "superuser",
>			"image_urls": null,
>			"date_created": "2023-06-28T12:14:30.737243Z",
>			"privacy": true,
>			"headline": "Happy Holidays",
>			"front_text": "From our family to yours",
>			"inner_text": "Love, Mr & Mr Mouse",
>			"likes": 150,
>			"background_color": "Blue",
>			"border_color": "Blue",
>			"border_decor": "Dotted",
>			"font_color": "Yellow",
>			"header_font": "Script",
>			"front_text_font": "Script",
>			"back_text_font": "Script"
>		 },


**request**
> DELETE  api/profile<username>/


**LIST ALL CARDS**

**request**
> GET  api/cards/

**reponse**
> list of cards:
>         {
>           "id": 11,,
>			"sent_by_user": "mouse",
>			"sent_to_user": "superuser",
>			"image_urls": null,
>			"date_created": "2023-06-28T12:14:30.737243Z",
>			"privacy": true,
>			"headline": "Happy Holidays",
>			"front_text": "From our family to yours",
>			"inner_text": "Love, Mr & Mr Mouse",
>			"likes": 150,
>			"background_color": "Blue",
>			"border_color": "Blue",
>			"border_decor": "Dotted",
>			"font_color": "Yellow",
>			"header_font": "Script",
>			"front_text_font": "Script",
>			"back_text_font": "Script"
>		 },

**request**
> POST  api/cards/
>         {
>			"sent_by_user": "mouse",
>			"sent_to_user": "superuser",
>			"headline": "Happy Holidays",
>			"front_text": "From our family to yours",
>			"inner_text": "Love, Mr & Mr Mouse",
>		 },

**response**
> 201_CREATED
>         {
>			"id": 11,,
>			"sent_by_user": "mouse",
>			"sent_to_user": "superuser",
>			"image_urls": null,
>			"date_created": "2023-06-28T12:14:30.737243Z",
>			"privacy": true,
>			"headline": "Happy Holidays",
>			"front_text": "From our family to yours",
>			"inner_text": "Love, Mr & Mr Mouse",
>			"likes": null,
>			"background_color": null,
>			"border_color": null,
>			"border_decor": null,
>			"font_color": null,
>			"header_font": null,
>			"front_text_font": null,
>			"back_text_font": null
>		 },


**SINGLE CARD**

**request**
> GET  api/profile/<int:pk>/

**response**
> single card: 
>         {
>			"id": 11,,
>			"sent_by_user": "mouse",
>			"sent_to_user": "superuser",
>			"image_urls": null,
>			"date_created": "2023-06-28T12:14:30.737243Z",
>			"privacy": true,
>			"headline": "Happy Holidays",
>			"front_text": "From our family to yours",
>			"inner_text": "Love, Mr & Mr Mouse",
>			"likes": 150,
>			"background_color": "Blue",
>			"border_color": "Blue",
>			"border_decor": "Dotted",
>			"font_color": "Yellow",
>			"header_font": "Script",
>			"front_text_font": "Script",
>			"back_text_font": "Script"
>		},

**request**
> PATCH  api/profile/<int:pk>/

**response**
> Changes made to card:
>        {
>			"id": 11,,
>			"sent_by_user": "mouse",
>			"sent_to_user": "superuser",
>			"image_urls": null,
>			"date_created": "2023-06-28T12:14:30.737243Z",
>			"privacy": true,
>			"headline": "Happy Holidays",
>			"front_text": "From our family to yours",
>			"inner_text": "Love, Mr & Mr Mouse",
>			"likes": 150,
>			"background_color": "Blue",
>			"border_color": "Blue",
>			"border_decor": "Dotted",
>			"font_color": "Yellow",
>			"header_font": "Script",
>			"front_text_font": "Script",
>			"back_text_font": "Script"
>		},

**request**
> DELETE  api/profile/<int:pk>/

**response**
> 204_NO_CONTENT


**CARDS SENT BY USER**

**request**
> GET  api/cards/sent/ 

**response**
> list of cards sent by user to other users
>         {
>			"id": 11,,
>			"sent_by_user": "mouse",
>			"sent_to_user": "superuser",
>			"image_urls": null,
>			"date_created": "2023-06-28T12:14:30.737243Z",
>			"privacy": true,
>			"headline": "Happy Holidays",
>			"front_text": "From our family to yours",
>			"inner_text": "Love, Mr & Mr Mouse",
>			"likes": 150,
>			"background_color": "Blue",
>			"border_color": "Blue",
>			"border_decor": "Dotted",
>			"font_color": "Yellow",
>			"header_font": "Script",
>			"front_text_font": "Script",
>			"back_text_font": "Script"
>		  },


**CARDS RECEIVED BY USER**

**request**
> GET  api/cards/received/ 

**response**
> list of cards received by user from other users
>         {
>			"id": 11,,
>			"sent_by_user": "mouse",
>			"sent_to_user": "superuser",
>			"image_urls": null,
>			"date_created": "2023-06-28T12:14:30.737243Z",
>			"privacy": true,
>			"headline": "Happy Holidays",
>			"front_text": "From our family to yours",
>			"inner_text": "Love, Mr & Mr Mouse",
>			"likes": 150,
>			"background_color": "Blue",
>			"border_color": "Blue",
>			"border_decor": "Dotted",
>			"font_color": "Yellow",
>			"header_font": "Script",
>			"front_text_font": "Script",
>			"back_text_font": "Script"
>		  },


**USER IS FOLLOWING**

**request**
> GET  api/user_following/

**response**
> list of users logged in user is following:
>   {
>	    "user_this_user_is_following": "mac"
>	},
>    {
>	    "user_this_user_is_following": "john"
>	},
>	{
>	    "user_this_user_is_following": "finn"
>	}


**USERS FOLLOWING LOGGED IN USER**

**request**
> GET  api/user_followers/

**response**
> list of users following logged in user:
>   { 
>		"this_user": "mac"
>	},
>	{
>		"this_user": "dylan"
>	}


**USER REQUEST TO FOLLOW ANOTHER USER**

**request**
> POST  api/follow_user/
> {
>	"user_this_user_is_following": "finn"
> }


**response**
> 201_CREATED
> {
>	"user_this_user_is_following": "finn"
> }

**USER REQEUST TO UNFOLLOW ANOTHER USER**

**request**
> DELETE  api/unfollow_user/<int:pk>/


**response**
> 204_NO_CONTENT 