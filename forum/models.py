from django.db import models
from django.utils import timezone

TAGS = [
    ('Genel', 'Genel'),
    ('Kediler', 'Kediler'),
    ('Köpekler', 'Köpekler'),
    ('Hamsterlar', 'Hamsterlar'),
    ('Sürüngenler', 'Sürüngenler'),
]

class ForumPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    tag = models.CharField(max_length=11 , choices=TAGS , default="Genel")

    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title


class ForumComments(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('ForumPost', related_name="comments" , on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

