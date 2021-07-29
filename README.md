## Music Player
Django based music player using database as source of songs
## Features
This project has functionality of Playing/Searching Songs, Playing/Creating/Deleting Playlists, Adding Songs to Playlists and Liking Songs
## Requirements
Django==3.2<br/>
Mysql==8.0.25 (or any other relational database of your choice)<br/>
mysqlclient==2.0.3 (python database connector of your respective relational database)

## Installation
```javascript
git clone https://github.com/him4lik/Music_Player.git
```
### Make following changes after cloning
#### Database settings(music_player/settings.py)
Replace values of ENGINE, NAME, USER, PASSWORD according to your database
```javascript
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'database_user',
        'PASSWORD': 'database_user_password',
    }
}
```
#### Initial Database Setup
Create User with email 'anoymous@anonymous.com'
![Screenshot from 2021-07-29 14-04-32](https://user-images.githubusercontent.com/75934883/127460157-4a8a6647-1fad-4916-88de-f9f691a56611.png)
Start server, Go to '/admin/', and add songs to 'songs' model for anonymous user created earlier<br/>
![Screenshot from 2021-07-29 13-57-20](https://user-images.githubusercontent.com/75934883/127459352-b9bf349b-9e6f-43de-8f78-1f5f3de6b6be.png)
Create a playlist named 'Top 5' and add songs to it for anonymous user created earlier
![Screenshot from 2021-07-29 13-57-55](https://user-images.githubusercontent.com/75934883/127459178-91f029f3-601d-4970-a3e0-164ed70ead2d.png)

## In Action
#### User Authentication
#### Play songs
#### Create/Delete Playlists
#### Add to Playlist
#### Like Songs
#### Search Songs
#### Dashboard
