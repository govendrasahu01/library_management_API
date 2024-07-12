from .models import *
from faker import Faker
import random

fack = Faker()

def add_author(n = 10):
    try:
        for i in range(n):
            first_name = fack.first_name()
            last_name = fack.last_name()
            
            yy = random.randint(1971,2000)
            mm = random.randint(1,12)
            dd = random.randint(1,30)
            
            date_of_birth = f'{yy}-{mm}-{dd}'
            
            bio = fack.text()
            
            Author.objects.create(
                first_name = first_name,
                last_name = last_name,
                date_of_birth = date_of_birth,
                bio = bio
            )
            
        print('success')
    except Exception as e:
        print(e)
        
        
def add_book(n = 10):
    try:
        for i in range(n):
            title = " ".join(fack.words())
            
            yy = random.randint(1971,2000)
            mm = random.randint(1,12)
            dd = random.randint(1,30)
            
            publication_date  = f'{yy}-{mm}-{dd}'
            number_of_pages = random.randint(80,400)
            
            all_authors = Author.objects.all()
            random_idx = random.randint(0,len(all_authors)-1)
            
            author = all_authors[random_idx]
            
            Book.objects.create(
                title = title,
                publication_date = publication_date,
                number_of_pages = number_of_pages,
                author = author
            )
        print('success')
    except Exception as e:
        print(e)

def add_member(n =10):
    
    try:
        for i in range(n):
            first_name = fack.first_name()
            last_name = fack.last_name()
            membership_date = '2024-07-10'
            email = None
            while not email:
                new = fack.email()
                data = Member.objects.filter(email = new)
                if not data.exists():
                    email = new
            Member.objects.create(
                first_name = first_name,
                last_name = last_name,
                membership_date = membership_date,
                email = email
            )
        print('success')
    except Exception as e:
        print(e)