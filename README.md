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

Using POST method in `<host>/api/add/`, put JSON in field with name `_content`.
JSON must have field `newapp`, which must have fields `Name` - it is name your app, `Des` - it is descriptor your app.

#### Pattern JSON:
```
{
"newapp":{
    "Name":"<name your app>",
    "Des": "<descriptor your app>"
        }
}
```
#### Example JSON:
```
{
"newapp":{
    "Name":"Vk_bot",
    "Des": "My first bot"
        }
}
```
This method answer `200` if app created and JSON, which will have `"success":"True"` and `"KeyApi": "1587603910.4631364"`
##### Example JSON answer:
```
{
    "success": "True",
    "KeyApi": "1587603910.4631364"
}
```
if app not add app you get `"seccess":"False"` and `"KeyApi":""`.
#### Example

```{
    "success": "False",
    "KeyApi": ""
}
```


