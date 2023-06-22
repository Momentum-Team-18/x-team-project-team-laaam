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
|Method  |URL                |Input                             |Output                                |Notes                                   |
|--------|-------------------|----------------------------------|--------------------------------------|----------------------------------------|
|LOGIN   |auth/token/login/  |{{User.USERNAME_FIELD}}, password |HTTP_200_OK, auth_token|token create  |                                        |
|LOGOUT  |auth/token/logout/ |   -                              |HTTP_204_NO_CONTENT                   |                                        |
|GET     |api/cards/         |   -                              |list of all cards                     |list                                    |
|GET     |api/cards/<int:pk> |   -                              |card info                             |retrieve card detail with specified pk  |
|POST    |api/cards/         |card data                         |new card                              |creates card                            |
|PATCH   |api/cards/<int:pk> |card data                         |updated card                          |updates card with specified pk          |
|DELETE  |api/cards/<int:pk> |   -                              |       -                              |deletes card with specified pk          |                    
|GET     |api/users/<int:pk> |  -                               |user info                             |*Do you want this to be a user profile? |



