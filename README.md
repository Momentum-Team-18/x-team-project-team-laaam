# Team LAAM BE README

**https://cards-q6a8.onrender.com**


**Token Authentication System**
* Djoser
* Docs: https://djoser.readthedocs.io/en/latest/introduction.html
  
**Deployment**
* Render
* Main Webservice Address: https://cards-q6a8.onrender.com
* Database: Postgresql@14
* Docs: https://render.com/docs/deploy-django
</br>
</br>


**CREATE USER**
> https://cards-q6a8.onrender.com/auth/users/

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
> https://cards-q6a8.onrender.com/auth/token/login

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
> https://cards-q6a8.onrender.com/auth/token/logout/

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
> https://cards-q6a8.onrender.com/api/profile/username/

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
DELETE  api/profile/<username>/
```

**response**
```json
204_NO_CONTENT
```

</br>
</br>

**ALL CARDS**
> https://cards-q6a8.onrender.com/api/cards/

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
</br>
</br>

**CREATE A CARD**
> https://cards-q6a8.onrender.com/api/cards/
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

**RETRIEVE, UPDATE, DELETE SINGLE CARD**
> https://cards-q6a8.onrender.com/api/cards/pk

*request*
```
GET api/profile/<int:pk>/
```

*response*

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
> https://cards-q6a8.onrender.com/api/cards/sent/

*request*
```json
GET  api/cards/sent/ 
```

*response*

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
> https://cards-q6a8.onrender.com/api/cards/received/

*request*
```json
GET  api/cards/received/ 
```

*response*

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
> https://cards-q6a8.onrender.com/api/user_following/

*request*
```json
GET  api/user_following/
```
*response*

```json
    {
      "user_this_user_is_following": "mac",
      "id": 8
    },
    {
      "user_this_user_is_following": "john",
      "id": 3
    },
    {
      "user_this_user_is_following": "finn",
      "id": 5
    }
```

</br>
</br>

**USERS FOLLOWING LOGGED IN USER**
> https://cards-q6a8.onrender.com/user_followers/

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
> https://cards-q6a8.onrender.com/api/follow_user/
> id is for follow relationship (not a user pk)
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
      "id": 28
    }
```
</br>
</br>

**USER REQUEST TO UNFOLLOW ANOTHER USER**
> https://cards-q6a8.onrender.com/unfollow_user/pk/
> pk is id of follow relationship (not a user pk)

*request*
```json
DELETE  api/unfollow_user/<int:pk>/
```

*response*
```json
204_NO_CONTENT 
```