from django.db import models
from django.utils import timezone

TAGS = [
    ('Genel', 'Genel'),
    ('Kediler', 'Kediler'),
    ('Köpekler', 'Köpekler'),
    ('Hamsterlar', 'Hamsterlar'),
    ('Sürüngenler', 'Sürüngenler'),
]

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumbnail = models.ImageField(upload_to='post/image/', null=True, blank=True)
    tag = models.CharField(max_length=11 , choices=TAGS , null=True , blank=True)

    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name="comments" , on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


