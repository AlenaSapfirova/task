from celery import shared_task
from .models import Subscribtion, Post



@shared_task
def print_posts():
    subscriptions = Subscribtion.objects.all()
    for subscription in subscriptions:
        author = subscription.author
        a = Post.objects.filter(author=author)
        latest_posts = Post.objects.filter(author=subscription.author).order_by('date_created')[:5]
        print(latest_posts)
        