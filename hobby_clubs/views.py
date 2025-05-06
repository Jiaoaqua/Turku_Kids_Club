import csv
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Club, Like, Review
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def index(request):
    """The home page for Hobby Log."""
    return render(request, 'hobby_clubs/index.html')


@login_required
def all_clubs(request):
    clubs = Club.objects.all() 
    return render(request, 'hobby_clubs/all_clubs.html', {'clubs': clubs})


@login_required
def science_clubs(request):
    science_clubs = Club.objects.filter(category='Science')
    return render(request, 'hobby_clubs/science_clubs.html', {'science_clubs': science_clubs})

@login_required
def art_clubs(request):
    art_clubs = Club.objects.filter(category='Art')
    return render(request, 'hobby_clubs/art_clubs.html', {'art_clubs': art_clubs})

@login_required
def sports_clubs(request):
    sports_clubs = Club.objects.filter(category='Sports')
    return render(request, 'hobby_clubs/sports_clubs.html', {'sports_clubs': sports_clubs})


def search_clubs(request):
    if request.method == 'GET':
        postal_code = request.GET.get('postcode')
        age = request.GET.get('age')
        club_type = request.GET.get('clubtype')
        
        matching_clubs = []

        with open('databasestore/clubs-info.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if (postal_code == row['Postal_Code'] and
                    age == row['Age'] and
                    club_type == row['Category']):
                    matching_clubs.append(row)
        if not matching_clubs:
            message = "Apologies, there are currently no clubs that match your criteria. Please try different search criteria."
            return render(request, 'hobby_clubs/search_results.html', {'message': message})
        
        return render(request, 'hobby_clubs/search_results.html', {'matching_clubs': matching_clubs})

from django.contrib.auth import logout

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        print("User loggedout")
        return redirect('hobby_clubs:index')
    return redirect('hobby_clubs:index') 
    
from django.shortcuts import render, get_object_or_404
from .models import Like, Club

@login_required
def like_club(request, club_name):
    club = get_object_or_404(Club, club_name=club_name)
    try:
        like, created = Like.objects.get_or_create(user=request.user, club=club)
        if created:
            message = 'You have successfully liked this club!'
        else:
            like.delete()
            message = 'You have successfully unliked this club!'
        return JsonResponse({'success': True, 'message': message})
    except Like.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Club not found'}, status=404)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # 如果使用 AJAX，确保处理 CSRF 问题或在前端设置正确的 CSRF token
def submit_review(request, club_name):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # 解析 JSON 数据
        content = data.get('content', '')
        club_name = data.get('clubName', club_name) 
        user = request.user
        club = get_object_or_404(Club, club_name=club_name)

        if not content:
            return JsonResponse({'success': False, 'error': 'Content cannot be empty'}, status=400)

        review = Review.objects.create(user=user, club=club, content=content)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)


@login_required
def user_profile(request):
    liked_clubs = Like.objects.filter(user=request.user).select_related('club')
    user_reviews = Review.objects.filter(user=request.user).select_related('club')
    return render(request, 'hobby_clubs/user_profile.html', {'user': request.user, 'liked_clubs': liked_clubs, 'user_reviews': user_reviews})




