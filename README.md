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
Start server, Go to '/admin/', and add songs to 'songs' model<br/>
Create a playlist named 'Top 5' and add songs to it

## In Action
#### User Authentication
#### Play songs
#### Create/Delete Playlists
#### Add to Playlist
#### Like Songs
#### Search Songs
#### Dashboard
