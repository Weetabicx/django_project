import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicbox.settings")

import django
django.setup()

from django.core.files import File
from django.contrib.auth.models import User
from user.models import UserProfile

def populate() -> None:
	print("Starting population script...")
	create_users()
	create_songs()
	create_albums()
	create_reviews()
	print("Population script ran successfully!")

def create_users() -> None:
	user_data = [
	{ "firstname": "usmaan", "lastname": "wahab"},
	{ "firstname": "james", "lastname": "macdonald"},
	{ "firstname": "harvey", "lastname": "olden"},
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

		user_profile = UserProfile.objects.create(user=user, picture="default.jpg")
		user_profile.save()
		

def create_songs() -> None:
	pass

def create_albums() -> None:
	pass 

def create_reviews() -> None:
	pass

if __name__ == "__main__":
	populate()