from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# from .data import books,users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from django.contrib.auth import get_user_model
from .models import Books, IssuedBooks
from .serializer import *
from rest_framework.response import Response

User= get_user_model()



# Create your views here.
class get_book_list_view(APIView):
    permission_classes= [permissions.IsAuthenticated]
    def get(self, request):
        queryset = Books.objects.all()
        # Check the books table is empty or not
        if queryset.exists() == False:
            Books.objects.bulk_create([
                Books(name='Dune', category='Science-Fiction'),
                Books(name='The Lost World', category='Science-Fiction'),
                Books(name='The Left Hand of Darkness', category='Science-Fiction'),
                Books(name='The Time Machine', category='Science-Fiction'),
                Books(name='Frankenstein', category='Science-Fiction'),
                Books(name='Things Fall Apart', category='Fiction'),
                Books(name='Beloved', category='Fiction'),
                Books(name='Alchemist', category='Fiction'),
                Books(name='The Catcher in the Rye', category='Fiction'),
                Books(name='Brave New World', category='Fiction'),
                Books(name='Tenaliraman', category='Fiction'),
                Books(name='Champak', category='Comedy'),
                Books(name='Catch-22', category='Comedy'),
                Books(name='Cruel Shoes', category='Comedy'),
                Books(name='Good Omens', category='Comedy'),

            ])

        books = Books.objects.all()
        books_list = []
        for book in  books:
            books_list.append({'book':book.name, 'category':book.category})
        
        return JsonResponse({'success':1, 'books':books_list})
       
        # return HttpResponse("Hello Test")

class add_book_view(APIView):
    permission_classes= [permissions.IsAuthenticated]
    def post(self, request):
        request_body=json.loads(request.body.decode('utf-8'))
        name=request_body['name']
        category=request_body['category']
        books = Books.objects.create(name=name, category=category)
        books.save()
        return JsonResponse({'success':1})
    
class issue_book_view(APIView):
    def post(self, request):
        request_body= json.loads(request.body.decode('utf-8'))
        user_email= request_body['user_email']
        book_name=request_body['book_name']
        issued_books= IssuedBooks.objects.create(user_email=user_email, book_name=book_name)
        issued_books.save()
        print('request recieved', request, request_body)
        return JsonResponse({'success':1})
    
class get_issued_book_view(APIView):
    def post(self, request):
        request_body= json.loads(request.body.decode('utf-8'))
        user_email= request_body['user_email']
        issued_books=IssuedBooks.objects.filter(user_email=user_email)
        issued_books_list = []
        for row in  issued_books:
            issued_books_list.append(row.book_name)
        return JsonResponse({'issued_books_list':issued_books_list})
    

# @csrf_exempt 
# def get_book_list_view(request):
#     print(request.COOKIES)
#     print(request.COOKIES.get('name'))
#     if(request.method == 'GET'):
#         return JsonResponse({'success':1, 'books':books})
#     return JsonResponse({'success':0})
    
# @csrf_exempt 
# def issue_book_view(request):
#     if(request.method == 'POST'):
#         request_body= json.loads(request.body.decode('utf-8'))
#         # Do processing
#         print('request recieved',request,request_body)
#         return JsonResponse(request_body)