import os, random
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicbox.settings")

import django
django.setup()

from django.core.files import File
from django.contrib.auth.models import User
from user.models import UserProfile
from album.models import Album, Album_Comment
from song.models import Song, Song_Comment


def populate() -> None:
	print("Starting population script...")
	create_users()
	create_albums()
	create_songs()
	create_reviews()
	print("Population script ran successfully!")

def create_users() -> None:
	user_data = [
	{ "firstname": "usmaan", "lastname": "wahab"},
	{ "firstname": "james", "lastname": "macdonald"},
	{ "firstname": "harvey", "lastname": "olden"},
    { "firstname": "tom", "lastname": "blunt"},
	]


	for data in user_data:
		firstname, lastname = data.values()
		user = User.objects.create(
			first_name=firstname, 
			last_name=lastname, 
			username=f"{firstname}_{lastname}", 
			email=f"{firstname}{lastname}@email.co.uk"
			)
		user.set_password(f"{firstname}123")
		user.save()

		user_profile = UserProfile.objects.create(user=user, picture="default/profile.jpg")
		user_profile.save()
		
def create_albums() -> None:
	album_data = [
		{ "name": "The Dark Side of the Moon", "type": "Album", "genre": "Progressive Rock", "release_date": "1973-03-01", "artist": "Pink Floyd"},
		{ "name": "Abbey Road", "type": "Album", "genre": "Rock", "release_date": "1969-09-26", "artist": "The Beatles"},
		{ "name": "The Wall", "type": "Album", "genre": "Progressive Rock", "release_date": "1979-11-30", "artist": "Pink Floyd"},
		{ "name": "Revolver", "type": "Album", "genre": "Rock", "release_date": "1966-08-05", "artist": "The Beatles"},
		{ "name": "Sgt. Pepper's Lonely Hearts Club Band", "type": "Album", "genre": "Rock", "release_date": "1967-06-01", "artist": "The Beatles"},
		{ "name": "The Beatles", "type": "Album", "genre": "Rock", "release_date": "1968-11-22", "artist": "The Beatles"},
		{ "name": "Cash in Cash out", "type": "Single", "genre": "Hip-Hop", "release_date": "2022-06-10", "artist": "Tyler, The Creator"},
		{ "name": "In My Room", "type": "EP", "genre": "Hip-Hop", "release_date": "2019-11-02", "artist": "Frank Ocean"},
		{"name": "Heaven's EP", "type": "EP", "genre": "Hip-Hop", "releae_date": "2022-06-10", "artist": "J. Cole"},
	]

	for data in album_data:
		album = Album.objects.create(
			name=data["name"],
			type=data["type"],
			genre=data["genre"],
			release_date=datetime.strptime(data["release_date"], "%Y-%m-%d"),
			artist=data["artist"],
			owner=User.objects.all()[random.randint(0, User.objects.count() - 1)],
			cover=f"default/album.jpg"
			)
		album.save()

def create_songs() -> None:
	for album in Album.objects.all():
		if album.type != "Album":
			song = Song.objects.create(
				title=album.name,
				genre=album.genre,
				release_date=album.release_date,
				artist=album.artist,
				album = album
				)
			song.save()
		else:
			for i in range(1, 11):
				song = Song.objects.create(
					title=f"{album.name} - Track {i}",
					genre=album.genre,
					release_date=album.release_date,
					artist=album.artist,
					album=album
					)
				song.save()

def create_reviews() -> None:
	for album in Album.objects.all():
		for i in range(1, 11):
			review = Album_Comment.objects.create(
				rating=random.randint(1, 10),
				comment=f"Comment {i}",
				album=album
				)
			review.save()

		for song in Song.objects.filter(album=album):
			review = Song_Comment.objects.create(
				rating=random.randint(1, 10),
				comment=f"Comment {1}",
				song=song
				)
			review.save()

if __name__ == "__main__":
	populate()