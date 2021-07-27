from django.urls import path, include
from main_site import views as main_site_views

urlpatterns=[
	path('', main_site_views.home, name='home'),
	path('auth/', include('custom_auth.urls')),
	path('like/<int:idd>/', main_site_views.like, name='like'),
	path('liked/', main_site_views.liked, name='liked'),
	path('create_playlist/', main_site_views.create_playlist, name='create_playlist'),
	path('search/', main_site_views.search.as_view(), name='search'),
	path('playlists/', main_site_views.playlists, name='playlists'),
	path('play_song/<int:idd>/', main_site_views.play_song, name='play_song'),
	path('play_liked/<int:idd>/', main_site_views.play_liked, name='play_liked'),
	path('playlist_songs/<int:idd>/', main_site_views.single_playlist, name='single_playlist'),
	path('play_playlist/<int:playlist_idd>/<int:song_idd>/', main_site_views.play_playlist, name='play_playlist'),
	path('remove_liked/<int:idd>/', main_site_views.remove_liked, name='remove_liked'),
	path('remove_playlist/<int:idd>/', main_site_views.remove_playlist, name='remove_playlist'),
	path('remove_from_playlist/<int:playlist_idd>/<int:song_idd>/', main_site_views.remove_from_playlist, name='remove_from_playlist'),
	path('playlists_to_add/<int:idd>/', main_site_views.show_playlists, name='show_playlists'),
	path('add_to_playlist/<int:playlist_idd>/<int:song_idd>/', main_site_views.add_to_playlist, name='add_to_playlist')
]