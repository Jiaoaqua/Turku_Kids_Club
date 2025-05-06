from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Club(models.Model):
    club_name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20) 
    address = models.CharField(max_length=255)
    age = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    activity = models.CharField(max_length=100)
    website = models.URLField(max_length=200)
    # unique_identifier = models.CharField(max_length=100, unique=True)

    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return self.club_name

    def calculate_average_rating(self):
        """Calculate the average rating"""
        average_rating = self.ratings.aggregate(Avg('rating'))['rating__avg']
        self.average_rating = round(average_rating, 2) if average_rating else 0.00
        self.save()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

