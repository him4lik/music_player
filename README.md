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
After this makemigrations and migrate them
```javascript
python manage.py makemigrations
python manage.py migrate
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
![auth (online-video-cutter com)](https://user-images.githubusercontent.com/75934883/127489631-22a6a0b3-e80e-4c9c-b86d-3301a1cc7905.gif)
#### Play songs
![playsong (online-video-cutter com)](https://user-images.githubusercontent.com/75934883/127489578-13feb445-0aa0-4221-802d-ba0204859511.gif)
#### Create/Delete Playlists
![createp (online-video-cutter com)](https://user-images.githubusercontent.com/75934883/127489609-59926c75-f6cd-41fe-a086-3dc2215dda3c.gif)
#### Add to Playlist
![addtop (online-video-cutter com)(1)](https://user-images.githubusercontent.com/75934883/127489654-a34b133e-a7a1-4220-89ed-d0b4aac09e41.gif)
#### Like Songs
![like (online-video-cutter com)](https://user-images.githubusercontent.com/75934883/127488786-ea75933c-b398-45f5-a24f-eaceddaf452d.gif)
#### Search Songs
![search (online-video-cutter com)](https://user-images.githubusercontent.com/75934883/127489592-19626b54-55a3-4285-b0f7-b459d3735ef3.gif)
#### Dashboard
![dash (online-video-cutter com)](https://user-images.githubusercontent.com/75934883/127489219-50664c66-26f7-4416-9b9e-c51b4e061329.gif)
