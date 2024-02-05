from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Subscribtion(models.Model):
    author = models.ForeignKey(User, related_name='author',
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'


class Post(models.Model):
    header = models.CharField(max_length=50)
    body = models.CharField(max_length=140)
    date_created = models.DateTimeField(auto_now=True,
                                        verbose_name='дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_post')
    is_read_it = models.BooleanField(default=False)
     
    def __str__(self):
        return self.header
