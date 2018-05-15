from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    BOY = 'B'
    GIRL = 'G'
    SEX = (
        (BOY, 'Boy'),
        (GIRL, 'Girl')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=SEX, default=BOY)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    avatar = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user

    def get_avatar(self):
        if not self.avatar:
            no_avatar = '/static/img/user.png'
            return no_avatar
        return self.avatar

def create_user_profile(sender, instance, created, **kw):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kw):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)