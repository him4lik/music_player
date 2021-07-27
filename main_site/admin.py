from django.contrib import admin
from main_site.models import song, playlist


class songadmin(admin.ModelAdmin):
	list_display = ('name', 'audio', 'artist')

class playlistadmin(admin.ModelAdmin):
	list_display = ('name', 'user', )


admin.site.register(song, songadmin)
admin.site.register(playlist, playlistadmin)