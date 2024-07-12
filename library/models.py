from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    bio = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_date  =models.DateField()
    number_of_pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    membership_date = models.DateField()
    email = models.EmailField(unique=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    
    def __str__(self) -> str:
         return f'{self.member.first_name} {self.member.last_name} -> {self.book.title}'