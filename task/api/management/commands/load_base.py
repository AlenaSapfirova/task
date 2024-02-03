from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from api.models import Post, Subscribtion
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'load base with mixer.blend'

    def handle(self, *args, **options):
        user = mixer.cycle(100).blend(User)
        post = mixer.cycle(100).blend(Post)
        subscribe = mixer.cycle(100).blend(Subscribtion)
        print(post, subscribe, user)