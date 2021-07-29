from django.shortcuts import render, redirect
from django import views
from django.core.paginator import Paginator
from .models import song, playlist
from django.contrib.auth.decorators import login_required
from .forms import search_form

#Home-Page
def home(request):
	play_list=playlist.objects.get(name='Top 5')
	songs=play_list.songs.all()
	paginator= Paginator(songs,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context={"page_obj":page_obj}
	return render(request,"main_site/home.html",context)

#Play song with give id
def play_song(request, idd):
	template_name='main_site/player.html'
	file=song.objects.filter(pk=idd)
	paginator= Paginator(file,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context={"page_obj":page_obj}
	return render(request, template_name, context)

#Search song
class search(views.View):
	template_name='main_site/search.html'
	form=search_form

	def get(self, request):
		fm=self.form()
		context={'form':fm}
		return render(request, self.template_name, context)

	def post(self, request):
		fm=self.form(request.POST)
		if fm.is_valid():
			search_key=fm.cleaned_data['search_key']
			songs_list=song.objects.filter(name__icontains=search_key)
			context={'form':fm, 'songs_list': songs_list}
			return render(request, self.template_name, context)
		context={'form':fm}
		return render(request, self.template_name, context)

#Like currently playing song
@login_required(login_url='login_user')
def like(request, idd):
	if request.GET.get('page'):
		redirect_to=request.GET.get('prev_page' )+"?page="+request.GET.get('page')
	else:
		redirect_to=request.GET.get('prev_page','' )
	file=song.objects.get(pk=idd)
	file.liked_by.add(request.user)
	print(redirect_to)
	print(request.GET.get('prev_page' ))
	return redirect(redirect_to)

#show liked songs by logged in user
@login_required(login_url='login_user')
def liked(request):
	template_name='main_site/liked.html'
	liked_songs=request.user.liked_songs.all()
	context={'liked':liked_songs}
	return render(request, template_name, context)

#Play all songs in liked by user starting with song with given id
@login_required(login_url='login_user')
def play_liked(request, idd):
	template_name='main_site/player.html'
	file=request.user.liked_songs.all()
	paginator= Paginator(file,1)
	if request.GET.get('page')==None:
		page=1
		for i in file:
			if i.id==idd:
				break
			page+=1
		page_number=page
	else:
		page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context={"page_obj":page_obj,'page_number':page_number}
	return render(request, template_name, context)

#Selecting playlists for adding currently playing song
@login_required(login_url='login_user')
def show_playlists(request, idd):
	template_name='main_site/show_playlists.html'
	playlists=request.user.playlist_set.all()
	context={'playlists':playlists, 'redir':request.GET.get('redir'), 'idd':idd, 'get_value':request.GET.get('get_value')}
	print(request.GET.get('get_value'))
	return render(request, template_name, context)

#Add given song(id) to given playlist(id)
@login_required(login_url='login_user')
def add_to_playlist(request, playlist_idd, song_idd):
	redirect_to=request.GET.get('redir' )+"?page="+request.GET.get('get_value')
	play_list=playlist.objects.get(pk=playlist_idd)
	song_file=song.objects.get(pk=song_idd)
	play_list.songs.add(song_file)
	return redirect(redirect_to)

#Show all playlists made by current user
@login_required(login_url='login_user')
def playlists(request):
	template_name='main_site/playlists.html'
	playlists=request.user.playlist_set.all()
	context={'playlists':playlists}
	return render(request, template_name, context)

#Show all songs in playlist with given id
@login_required(login_url='login_user')
def single_playlist(request, idd):
	template_name='main_site/single_playlist.html'
	obj=playlist.objects.get(pk=idd)
	songs=obj.songs.all()
	context={'songs':songs, 'idd':idd}
	return render(request, template_name, context)

#Play playlist with given id starting with song of given id
@login_required(login_url='login_user')
def play_playlist(request, playlist_idd, song_idd):
	template_name='main_site/player.html'
	obj=playlist.objects.get(pk=playlist_idd)
	file=obj.songs.all()
	paginator= Paginator(file,1)
	if request.GET.get('page')==None:
		page=1
		for i in file:
			if i.id==song_idd:
				break
			page+=1
		page_number=page
	else:
		page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context={"page_obj":page_obj,'page_number': page_number, 'playlist_name':obj.name}
	return render(request, template_name, context)

#Delete playlist with given id
@login_required(login_url='login_user')
def remove_playlist(request, idd):
	obj=playlist.objects.get(pk=idd)
	obj.delete()
	return redirect('playlists')

#Delete given song(id) from given playlist(id)
@login_required(login_url='login_user')
def remove_from_playlist(request, playlist_idd, song_idd):
	obj=playlist.objects.get(pk=playlist_idd)
	song_file=song.objects.get(pk=song_idd)
	obj.songs.remove(song_file)
	return redirect(request.GET.get('path'))

#Create playlist for current user
@login_required(login_url='login_user')
def create_playlist(request):
	if request.method=='POST':
		value=request.POST.get('new_playlist')
		playlist.objects.create(name=value, user=request.user)
		try:
			request.POST['path']
			return redirect(request.POST['path']+'?redir='+request.POST['redir']+'&get_value='+request.POST['get_value'])
		except:
			return redirect('playlists')

#Remove song with given id from liked songs
@login_required(login_url='login_user')
def remove_liked(request, idd):
	audio_file=song.objects.get(pk=idd)
	audio_file.liked_by.remove(request.user)
	return redirect('liked')
