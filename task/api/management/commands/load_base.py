from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from api.models import Post, Subscribtion
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'load base with mixer.blend'

    def handle(self, *args, **options):
        for _ in range(1000):
            user = mixer.blend(User)
            post = mixer.blend(Post)
            subscribe = mixer.blend(Subscribtion)
            user.save()
            post.save()
            subscribe.save()
        print('Загрузка завершена')