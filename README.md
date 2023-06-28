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



**CREATE USER**

*request*
```json
POST  auth/users/
    {
    "username": "superuser",
    "password": "somepassword"
    }
```

*response*
```json
HTTP_201_created
    {
    "username": "superuser",
    "password": "somepassword",
    "id": 1
    }
```
</br>
</br>

**LOGIN**

*request*
```json
POST auth/token/login/
    {
    "username": "superuser",
    "password": "somepassword"
    }
```

*response*
```json
HTTP_200_OK
    {
    "auth_token": "somereallylonglistofnumbersandletters"
    }
```
</br>
</br>


**LOGOUT**

*request*
```json
POST auth/token/logout/
```

*response*
```json
HTTP_204_NO_CONTENT
```

</br>
</br>

**PROFILE**

*request*
```json
GET api/profile/<username>/
```

*response*
```json
    {
    "username": "superuser",
    "first_name": "",
    "last_name": "",
    "bio": null,
    "date_joined": "2023-06-26T23:45:36.884115Z",
    "cards_sent": [
        {
        "id": 12,
        "sent_by_user": "superuser",
        "sent_to_user": "mouse",
        "image_urls": null,
        "date_created": "2023-06-27T12:14:01.348168Z",
        "privacy": true,
        "headline": "Hello!",
        "front_text": "I miss you.",
        "inner_text": "Love, Mouse",
        "likes": 15,
        "background_color": "Blue",
        "border_color": "Red",
        "border_decor": "Solid",
        "font_color": "Black",
        "header_font": "Script",
        "front_text_font": "Script",
        "back_text_font": "Script"
         },
    ],
    "cards_received": [
        {
        "id": 11,,
        "sent_by_user": "mouse",
        "sent_to_user": "superuser",
        "image_urls": null,
        "date_created": "2023-06-28T12:14:30.737243Z",
        "privacy": true,
        "headline": "Happy Holidays",
        "front_text": "From our family to yours",
        "inner_text": "Love, Mr & Mr Mouse",
        "likes": 150,
        "background_color": "Blue",
        "border_color": "Blue",
        "border_decor": "Dotted",
        "font_color": "Yellow",
        "header_font": "Script",
        "front_text_font": "Script",
        "back_text_font": "Script"
        },
    ]
}
```
*request*
```json
PATCH  api/profile/<username>/
```

*response*
> Any changes made to profile:
```json
    {
    "id": 11,,
    "sent_by_user": "mouse",
    "sent_to_user": "superuser",
    "image_urls": null,
    "date_created": "2023-06-28T12:14:30.737243Z",
    "privacy": true,
    "headline": "Happy Holidays",
    "front_text": "From our family to yours",
    "inner_text": "Love, Mr & Mr Mouse",
    "likes": 150,
    "background_color": "Blue",
    "border_color": "Blue",
    "border_decor": "Dotted",
    "font_color": "Yellow",
    "header_font": "Script",
    "front_text_font": "Script",
    "back_text_font": "Script"
    },
```

*request*
```json
DELETE  api/profile</username>/
```

</br>
</br>

**LIST ALL CARDS**

*request*
```json
GET  api/cards/
```

*response*
> list of cards:
```json
        {
        "id": 11,,
        "sent_by_user": "mouse",
        "sent_to_user": "superuser",
        "image_urls": null,
        "date_created": "2023-06-28T12:14:30.737243Z",
        "privacy": true,
        "headline": "Happy Holidays",
        "front_text": "From our family to yours",
        "inner_text": "Love, Mr & Mr Mouse",
        "likes": 150,
        "background_color": "Blue",
        "border_color": "Blue",
        "border_decor": "Dotted",
        "font_color": "Yellow",
        "header_font": "Script",
        "front_text_font": "Script",
        "back_text_font": "Script"
        },
```

*request*
```json
POST  api/cards/
        {
        "sent_by_user": "mouse",
        "sent_to_user": "superuser",
        "headline": "Happy Holidays",
        "front_text": "From our family to yours",
        "inner_text": "Love, Mr & Mr Mouse",
        },
```
*response*
```json
201_CREATED
        {
        "id": 11,,
        "sent_by_user": "mouse",
        "sent_to_user": "superuser",
        "image_urls": null,
        "date_created": "2023-06-28T12:14:30.737243Z",
        "privacy": true,
        "headline": "Happy Holidays",
        "front_text": "From our family to yours",
        "inner_text": "Love, Mr & Mr Mouse",
        "likes": null,
        "background_color": null,
        "border_color": null,
        "border_decor": null,
        "font_color": null,
        "header_font": null,
        "front_text_font": null,
        "back_text_font": null
        },
```

</br>
</br>

**SINGLE CARD**

*request*
```
GET  api/profile/<int:pk>/
```

*response*
> single card: 
```json
        {
        "id": 11,,
        "sent_by_user": "mouse",
        "sent_to_user": "superuser",
        "image_urls": null,
        "date_created": "2023-06-28T12:14:30.737243Z",
        "privacy": true,
        "headline": "Happy Holidays",
        "front_text": "From our family to yours",
        "inner_text": "Love, Mr & Mr Mouse",
        "likes": 150,
        "background_color": "Blue",
        "border_color": "Blue",
        "border_decor": "Dotted",
        "font_color": "Yellow",
        "header_font": "Script",
        "front_text_font": "Script",
        "back_text_font": "Script"
        },
```

*request*
```json
PATCH  api/profile/<int:pk>/
```

*response*
> Any changes made to card:
```json
    {
    "id": 11,,
    "sent_by_user": "mouse",
    "sent_to_user": "superuser",
    "image_urls": null,
    "date_created": "2023-06-28T12:14:30.737243Z",
    "privacy": true,
    "headline": "Happy Holidays",
    "front_text": "From our family to yours",
    "inner_text": "Love, Mr & Mr Mouse",
    "likes": 150,
    "background_color": "Blue",
    "border_color": "Blue",
    "border_decor": "Dotted",
    "font_color": "Yellow",
    "header_font": "Script",
    "front_text_font": "Script",
    "back_text_font": "Script"
    }
```
*request*
```json
DELETE  api/profile/<int:pk>/
```

*response*
```json
204_NO_CONTENT
```

</br>
</br>

**CARDS SENT BY USER**

*request*
```json
GET  api/cards/sent/ 
```

*response*
> list of cards sent by user to other users
```json
    {
    "id": 11,
    "sent_by_user": "mouse",
    "sent_to_user": "superuser",
    "image_urls": null,
    "date_created": "2023-06-28T12:14:30.737243Z",
    "privacy": true,
    "headline": "Happy Holidays",
    "front_text": "From our family to yours",
    "inner_text": "Love, Mr & Mr Mouse",
    "likes": 150,
    "background_color": "Blue",
    "border_color": "Blue",
    "border_decor": "Dotted",
    "font_color": "Yellow",
    "header_font": "Script",
    "front_text_font": "Script",
    "back_text_font": "Script"
    }
```
</br>
</br>

**CARDS RECEIVED BY USER**

*request*
```json
GET  api/cards/received/ 
```

*response*
> list of cards received by user from other users
```json
        {
        "id": 11,,
        "sent_by_user": "mouse",
        "sent_to_user": "superuser",
        "image_urls": null,
        "date_created": "2023-06-28T12:14:30.737243Z",
        "privacy": true,
        "headline": "Happy Holidays",
        "front_text": "From our family to yours",
        "inner_text": "Love, Mr & Mr Mouse",
        "likes": 150,
        "background_color": "Blue",
        "border_color": "Blue",
        "border_decor": "Dotted",
        "font_color": "Yellow",
        "header_font": "Script",
        "front_text_font": "Script",
        "back_text_font": "Script"
        }
```
</br>
</br>

**USER IS FOLLOWING**

*request*
```json
GET  api/user_following/
```
*response*
> list of users logged in user is following:
```json
    {
    "user_this_user_is_following": "mac"
    },
    {
    "user_this_user_is_following": "john"
    },
    {
        "user_this_user_is_following": "finn"
    }
```

</br>
</br>

**USERS FOLLOWING LOGGED IN USER**

*request*
```json
GET  api/user_followers/
```

*response*
list of users following logged in user:
```json
    { 
      "this_user": "mac"
    },
    {
      "this_user": "dylan"
    }
```

</br>
</br>

**USER REQUEST TO FOLLOW ANOTHER USER**

*request*
```json
POST  api/follow_user/
    {
      "user_this_user_is_following": "finn"
    }
```

*response*
```json
201_CREATED
    {
      "user_this_user_is_following": "finn"
    }
```
</br>
</br>

**USER REQUEST TO UNFOLLOW ANOTHER USER**

*request*
```json
DELETE  api/unfollow_user/<int:pk>/
```

*response*
```json
204_NO_CONTENT 
```