from faker import Faker
from models import Author
import random
from rest_framework import serializers
import os

print(Author)


# for i in range(100):
#     fake = Faker()
#     spam = str(fake.name()).split()
#     num_birth = random.randint(1800, 2002)

#     author1 = Author.objects.create(first_name=spam[0],last_name=spam[1], birthday_year=num_birth, email=f"{spam[0]}{num_birth}@bk.ru")
