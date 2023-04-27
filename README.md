# Social Media API

API service for social media written on DRF

## Installing using GitHub
```python
git clone https://github.com/SlavikSherbak/social_media_API.git
cd social_media_API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
set SECRET_KEY=<your secret key>
python manage.py migrate
python manage.py runserver
```

## Getting access
```python
create user via /api/user/register/
get access token via /api/user/token/
```

## Features
- create profiles
- follow other users
- create and retrieve posts
- perform basic social media actions
