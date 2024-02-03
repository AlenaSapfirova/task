from celery import shared_task
from .models import Subscribtion, Post
from django.core.mail import send_mail
from task.settings import EMAIL_HOST_USER



@shared_task
def print_posts():
    subscriptions = Subscribtion.objects.all()
    for subscription in subscriptions:
        latest_posts = Post.objects.filter(author=subscription.author).order_by('date_created')[:5]
        message = [post.header for post in latest_posts]
        print(message)
        print('Подборка отправлена пользователю')