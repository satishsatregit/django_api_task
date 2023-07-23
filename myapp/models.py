from django.core.validators import MinValueValidator
from django.db import models

class user(models.Model):
    user_ID = models.CharField(max_length=100,validators=[MinValueValidator(limit_value=2)])
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    other_relevant_details = models.CharField(max_length=100)

    def __str__(self):
        return self.user_ID

    class Meta:
        db_table = 'user'


class BlogPost(models.Model):
    post_id = models.CharField(max_length=100,validators=[MinValueValidator(limit_value=2)])
    title = models.TextField()
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    other_relevent_details = models.TextField()

    def __str__(self):
        return self.post_id

    class Meta:
        db_table = 'Bogpost'

class like(models.Model):
    like_id = models.CharField(max_length=100)
    post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.like_id

    class Meta:
        db_table = 'like'

