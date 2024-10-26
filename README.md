# x-api
Twitter Feed API

## TO DO
### pre-requisites
(on Mac)
1. brew install python@3.10
2. python3.10 -m venv virtualenv
### (else)
1. python -m venv virtualenv
### app package install and startup
2. source ./virtualenv/bin/activate
3. pip -i requirements.txt
4. edit .env and add twitter bearer token from x api developer apps web page
4. python xapi.py 

### workaround for finding api user id from x.com site
1. Open Chrome browser, developer tools, go to Networking tab
2. Navigate to `https://x.com/sama` substituting the username
3. Search for `UserByScreenName` api request using the Filter in the Networking tab
4. Click Response tab
5. Examine the http response json object for rest_id field (data.user.result.rest_id). In this case the userid is `1605`
```
{
    "data": {
        "user": {
            "result": {
                "__typename": "User",
                "id": "VXNlcjoxNjA1",
                "rest_id": "1605",
                "affiliates_highlighted_label": {},
                "has_graduated_access": true,
                "is_blue_verified": true,
                "profile_image_shape": "Circle",
```
