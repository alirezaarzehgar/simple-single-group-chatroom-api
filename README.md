## Introduction
this is an smal project that i push v.0.0.1
you can run it on your server and use from it.

# installing

$ `pip install -r requirement.txt`
$ `python app.py`

# API documention

## Register

- URL

`/api/register`

- Method

POST

- DATA Params
```
username
password
first_name
last_name
profile -> you shod upload profile and modify this param
```

- Success Response

Code: `201`

Content: `{"message": "user created successfully"}`

- Error Response

Code: `500`

Content: `{"message": "Internal server error mybe database problem"}`

Code: `409`

Content: `{"message": "user already in use"}`

## Login

- URL

`/api/login`

- Method

POST

- DATA Params

```
username
password
```

- Success Response 

Code: `202`

Content: `{"access_token": "token", "message": "login succeeded"}`

- Error Response

Code: `403`
Content: `"message": "bad username or password"}`


## User

- URL

`/api/user`

- Methods

GET

- token is required

- Data Params

```
id
```

- Success Response

Code: `200`

Content: 
```
{
    "message": [
        {
            "ID": 1,
            "first_name": "alireza",
            "last_name": "arzehgar",
            "password": "!@#$",
            "profile": null,
            "username": "alirezaarzehgar"
        }
    ]
}
```

- Error Response

Code: `422`

Content: `{"msg": "Invalid header padding"}`

Code: `401`

Content: `{"msg": "Token has expired"}`

- Method

- token is required

PUT

- Data Params

filling all parameters is unnecessary.
you can modify every parameter that you want

```
username
password
first_name
last_name
profile
```

- Success Response

Code: `201`

Content: `{"message": "user info modyfied successfully"}`

- Error Response

Code: `404`

Content: `{"message": "user dose not exists"}`

Code: `422`

Content: `{"msg": "Invalid header padding"}`

Code: `401`

Content: `{"msg": "Token has expired"}`

- Method
delete current user account

DELETE

- Success Response

Code: `200`

Content: `{"message": "deleted successfully"}`

- Error Response

Code: `402`

Content: `{"message": "user dose not exists"}`

Code: `422`

Content: `{"msg": "Invalid header padding"}`

Code: `401`

Content: `{"msg": "Token has expired"}`


## Upload

- URL

`/api/upload`

- token is required

- Methods

POST

- Data Params
```
type -> String
file -> Browse file
```

- Success Response

Code: `200`

Content: `{"message": "uploaded file successfully"}`

- Error Response

Code: `404`

Content: `{"message": "missing file"}`

Code: `422`

Content: `{"msg": "Invalid header padding"}`

Code: `401`

Content: `{"msg": "Token has expired"}`


## Download

- URL

`/api/download`

- token is required

- Method

GET

- Data Params

```
name
type
```

- Success Response

Code: `200`

Content: `{file-type}`

- Error

Code: `404`

Content: `{"message": "your file not found"}`

Code: `422`

Content: `{"msg": "Invalid header padding"}`

Code: `401`

Content: `{"msg": "Token has expired"}`


## Message

- URL

`/api/message`

- token is required

- Methods

POST

- Data Params

```
text
file_type
file_name
```

- Success Response

Code: `200`

Content: `{"message": "message sent successfully"}`

- Error Response

Code: `404`

Content: `{"message": "your file or format not found"}`

Code: `404`

Content: `{"message": "invalid type of name"}`

Code: `404`

Content: `{"message": "cant send message"}`

Code: `422`

Content: `{"msg": "Invalid header padding"}`

Code: `401`

Content: `{"msg": "Token has expired"}`

- Methods

GET

- Success
getting all messages

code: `200`

Content: `{"message": { ... }}`
