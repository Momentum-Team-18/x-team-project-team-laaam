# Team LAAM BE README

**Token Authentication System**
* Djoser
* Docs: https://djoser.readthedocs.io/en/latest/introduction.html
  
**Deployment**
* Render
* Main Webservice Address: https://cards-q6a8.onrender.com
* Database: Postgresql@14
* Docs: https://render.com/docs/deploy-django

**Create User**
|Method  |URL                |Request                           |Response                      |                               
|--------|-------------------|----------------------------------|------------------------------|
|POST    |auth/users/        |{{ User.USERNAME_FIELD }}         |HTTP_201_CREATED:             |
|        |                   |{{ User.REQUIRED_FIELDS }}        |{{ User.USERNAME_FIELD }}     |
|        |                   |password                          |{{ User._meta.pk.name }}      |
|        |                   |re_password                       |{{ User.REQUIRED_FIELDS }}    |
|        |                   |                                  |------------------------------|
|        |                   |                                  |HTTP_400_BAD_REQUEST:         |     
|        |                   |                                  |{{ User.USERNAME_FIELD }}     |
|        |                   |                                  |{{ User.REQUIRED_FIELDS }}    |
|        |                   |                                  |password                      |
|        |                   |                                  |re_password                   |

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