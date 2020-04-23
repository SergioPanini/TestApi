# TestApi


## How to install 

That run project you need have python 3 and git for download project.

### How to download
Use `git clone https://github.com/SergioPanini/TestApi.git` for download projects. 

### How to run
1) Install python libraries use `pip install django` and `pip install djangorestframework`.
2) Use `cd TestApi/Flower` for move project's folder.  
3) Use `python3 manage.py runserver` for run local server. it is working on 127.0.0.1:8000.  


## API

All methods contain in `<host>/api/` and use JSON marking .

### Add app

First step is add new app in system and get `KeyApi` token that work this your app.

Using `POST` method in `<host>/api/add/`, put JSON data in field with name `_content`.
JSON data must have field `"newapp"`, which must have fields `"Name"` - it is name your app, `"Des"` - it is descriptor your app.

#### Code answer:
200

#### Pattern JSON:
```
{
"newapp":{
    "Name":"<name your app>",
    "Des": "<descriptor your app>"
        }
}
```

#### Example:
```
{
"newapp":{
    "Name":"Vk_bot",
    "Des": "My first bot"
        }
}
```

This method answer `200`, if app created and JSON, which will have `"success":"True"` and `"KeyApi": "1587603910.4631364"`

##### Example JSON answer:
```
{
    "success": "True",
    "KeyApi": "1587603910.4631364"
}
```

if app not add app you get `"seccess":"False"` and `"KeyApi":""`.

#### Example:
```{
    "success": "False",
    "KeyApi": ""
}
```
### Get info about app

Using `Get` method in `<host>/api/test/<KeyAPi>` for get info about your app.`<KeyApi>` - it is `KeyApi` token your app. You get JSON in answer. 
if `KeyApi` token is True, JSON answer will have field `"app"`, whitch will have fields `"Name"` - it is name your app, `"Des"` - it is description your app and `"KeyApi"` - it is tiken your app.

#### Code answer:
200 or 404

#### Example:
```
{
    "app": {
        "Name": "ddddddd",
        "Des": "ffffffffffffffgggggggg",
        "KeyApi": "1587599498.6985188"
    }
}
```

If `KeyApi` token is False, JSON answer will have field `"detail"` and you get code 404.

#### Example
```{
    "detail": "Not found."
}
```

### Update data

You can update data about your app use method `PUT` in `<host>/api/test/<KeyApi>`. Put JSON data in field with name `_content`.
JSON data must have field `"updateapp"`, which can have fields `"Name"` - it is name your app, `"Des"` - it is descriptor your app. 

if data is true you will have JSON answer with field `"seccees"` and it always is True. Fileds `"Name"` or `"Des"` will be empty.


#### Code answer:
200 or 404

#### Example:
```
{
    "success": "True"
}
```

### Delete app

You must send `DELETE` method in `<host>/api/test/<KeyApi>`. You get answer as JSON data.
Filed `"seccess"` always will `"True"`.

#### Code answer:
200 or 404

#### Example
```
{
    "seccess": true
}
```

### Get New token

To update the token use `GET` method in `<host>/api/updatekey/`. You get JSON answer, which will have new 
`"KeyApi"` token your app.

#### Code answer:
200

#### Example:
```
{
    "seccess": true,
    "NewKeyApi": 1587599583.5333102
}
```
