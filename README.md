# Instagram
## Get insagram profile from userID
___
### Get the tokens from browser cookie store after logging into Insta.
```
loader.load_session("username", {
    "csrftoken": "", 
    "sessionid": "",
    "ds_user_id": "",
    "mid": "",
    "ig_did": ""
})

```
### **If you using instaloader  V4.14.1**

### 1. Go into your .venv/Lib/site-packages/instaloader folder.\
### 2. Open instaloadercontext.py\
### 3. Seach for "def login(self, user, passwd):"\
### 4. Delete 'sessionid': '', from\
```
session.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1',
                        'ig_vw': '1920', 'ig_cb': '1', 'csrftoken': '',
                         's_network': '', 'ds_user_id': ''})
```
### so you get: 
```
session.cookies.update({'mid': '', 'ig_pr': '1',
                                'ig_vw': '1920', 'ig_cb': '1', 'csrftoken': '',
                                's_network': '', 'ds_user_id': ''})
```