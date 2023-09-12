from django.urls import path,include
from .views import *
urlpatterns = [
    path('booklist',get_book_list_view.as_view()),
    path('issuebook',issue_book_view.as_view()),
    path('addbook',add_book_view.as_view()),
    path('getissuedbooks',get_issued_book_view.as_view()),
]