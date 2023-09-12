from django.urls import path,include
from .views import *
urlpatterns = [
    # path('',render_test),
    path('',render_home_page),

]