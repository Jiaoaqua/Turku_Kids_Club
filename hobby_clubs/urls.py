'''Defines URL patterns for hobby_clubs'''
from django.urls import path
from . import views
from .views import logout_view
<<<<<<< HEAD
=======
from django.urls import re_path

>>>>>>> 2dcc16a (Update project files)
from django.contrib.auth import views as auth_views

# from .views import rate_club



app_name = 'hobby_clubs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

<<<<<<< HEAD


=======
>>>>>>> 2dcc16a (Update project files)
    path('search/', views.search_clubs, name='search_clubs'),

    path('logout/', logout_view, name='logout'),

    path('all-clubs/', views.all_clubs, name='all_clubs'),

<<<<<<< HEAD
    # path('science-clubs/', views.science_clubs, name='science_clubs'),
=======
    path('science-clubs/', views.science_clubs, name='science_clubs'),

    path('art-clubs/', views.art_clubs, name='art_clubs'),

    path('sports-clubs/', views.sports_clubs, name='sports_clubs'),
>>>>>>> 2dcc16a (Update project files)

    path('user/profile/', views.user_profile, name='user_profile'),

    path('like-club/<str:club_name>/', views.like_club, name='like_club'),

<<<<<<< HEAD
    path('user/profile/password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),

]


=======
    re_path(r'^submit_review/(?P<club_name>[\w\s\-]+)/$', views.submit_review, name='submit_review'),
]




>>>>>>> 2dcc16a (Update project files)
