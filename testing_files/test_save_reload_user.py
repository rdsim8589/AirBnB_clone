#!/usr/bin/python3
from models import storage, base_model, user, amenity, city, state, place, review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = user.User()
my_user.first_name = "Betty"
my_user.last_name = "Holberton"
my_user.email = "airbnb@holbertonshool.com"
my_user.password = "root"
my_user.save()
print(my_user)

my_city = city.City()
my_city.name = "San Francisco"
my_city.state_id = "101"
my_city.save()
print(my_city)

my_state = state.State()
my_state.name = "california"
my_state.save()
print(my_state)

my_place = place.Place()
my_place.number_rooms = 3
my_place.max_guest = 2
my_place.price_by_night = 100
my_place.save()
print(my_place)

my_amenity = amenity.Amenity()
my_amenity.name = "House Keeping"
my_amenity.save()
print(my_amenity)

my_review = review.Review()
my_review.text = "Its a good place."
my_review.save()
print(my_review)
