from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('',views.peop,name='peop')

    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='about')
    # path('add/',views.addition,name='addition')
]
