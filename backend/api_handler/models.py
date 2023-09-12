from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=255)
    category=models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    
class IssuedBooks(models.Model):
    user_email=models.EmailField(max_length=255)
    book_name=models.CharField(max_length=255)

    def __str__(self):
        return str(self.user_email)+ str(self.book_name)
    
