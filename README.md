# WellDone
WellDone: KeepCoding bootcamp final practise

To install dependences, with the environment activate:
```pip install -r requirements.txt```

####API ENDPOINTS
#####Create user (Signup)
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
#####Delete user
*DELETE /api/0.1/delete_user/id_user*

To delete a user, send a DELETE request to /api/0.1/delete_user/id_user.

Result:
```

```