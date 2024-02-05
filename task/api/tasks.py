from celery import shared_task
from .models import Subscribtion, Post


@shared_task
def print_posts():
    subscriptions = Subscribtion.objects.all()
    for subscription in subscriptions:
        latest_posts = Post.objects.filter(author=subscription.author).order_by('date_created')[:5]
        for post in latest_posts:
            print(post.header)
        print('Подборка пользователю отправлена')
