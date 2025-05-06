'''Defines URL patterns for hobby_clubs'''
from django.urls import path
from . import views
from .views import logout_view
from django.urls import re_path

from django.contrib.auth import views as auth_views

# from .views import rate_club



app_name = 'hobby_clubs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    path('search/', views.search_clubs, name='search_clubs'),

    path('logout/', logout_view, name='logout'),

    path('all-clubs/', views.all_clubs, name='all_clubs'),

    path('science-clubs/', views.science_clubs, name='science_clubs'),

    path('art-clubs/', views.art_clubs, name='art_clubs'),

    path('sports-clubs/', views.sports_clubs, name='sports_clubs'),

    path('user/profile/', views.user_profile, name='user_profile'),

    path('like-club/<str:club_name>/', views.like_club, name='like_club'),

    re_path(r'^submit_review/(?P<club_name>[\w\s\-]+)/$', views.submit_review, name='submit_review'),
]




