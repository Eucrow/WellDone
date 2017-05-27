# WellDone
WellDone: KeepCoding bootcamp final practise

To install dependences, with the environment activate:
```pip install -r requirements.txt```

#### API ENDPOINTS

To use the API Gateway, are available the django-rest-auth endpoints:

##### Registration
* rest-auth/registration/ (POST)
    * username
    * password1
    * password2
    * email

Return:
```
{
  "token": "jwt token",
  "user": {
    "pk": 20,
    "username": "username",
    "email": "email@email.com",
    "first_name": "first_name",
    "last_name": "last_name"
  }
}
```

##### Login
* /rest-auth/login/ (POST)
    * username
    * email
    * password

Return:
```
{
  "token": "jwt token",
  "user": {
    "pk": pk,
    "username": "username",
    "email": "email@email.com",
    "first_name": "first_name",
    "last_name": "last_name"
  }
}
```
#### Delete user
Only user can delete its own user.

* /api/delete_user/id (DELETE)
    * Authorization header with JWT token must be send.

Return:
```
{
  "Message": "Usuario borrado"
}
```

#### Get user info
Obtain user info. The user must be authenticated.

* /api/rest-auth/user/ (GET)
    * Authorization header with JWT token must be send.

Return:
```
{
    "pk": pk,
    "username": "username",
    "email": "email@email.com",
    "first_name": "first_name",
    "last_name": "last_name"
}
```

#### Update user info
Update user info. The user must be authenticated.

* /api/rest-auth/user/ (GET)
    * Authorization header with JWT token must be send.
    * JSON with updated data:
```
    "username": "new_username",
    "email": "new_email@email.com",
    "first_name": "new_first_name",
    "last_name": "new_last_name"
```

Return:
```
{
    "pk": pk,
    "username": "new_username",
    "email": "new_email@email.com",
    "first_name": "new_first_name",
    "last_name": "new_last_name"
}
```

#### Internationalization
To use internationalization import:

```
from django.utils.translation import ugettext as _
```

Use example:

```
message = {'Message': _('User deleted')}
```


<!---
##### Create user (Signup)

*POST /api/0.1/signup*

To create a new user send a POST request to /api/0.1/signup with input body: { 'username', 'first_name', 'last_name', 'email', 'password' }

Result:
```
{
  "username": "my_username",
  "first_name": "my_first_name",
  "last_name": "my_last_name",
  "email": "my_email@amez.info",
  "password": "pbkd..."
}
```
##### Delete user

*DELETE /api/0.1/delete_user/id_user*

To delete a user, send a DELETE request to /api/0.1/delete_user/id_user.

Result:
```
"User deleted"
```
--->