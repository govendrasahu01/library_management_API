from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('author/',views.author.as_view()),
    path('author/<int:pk>/',views.del_update_author.as_view()),
    path('auth-detail/<int:id>/',views.auth_detail),
    
    path('book/',views.book.as_view()),
    
    path('member/',views.member.as_view()),
    path('member-detail/<int:id>/', views.member_datail),
    
    path('borrow/',views.borrow_book.as_view()),
    path('return-book/<int:id>/', views.return_book)
    
]
