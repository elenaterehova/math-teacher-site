from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class SocialMedia(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название соц.сети')
    social_url = models.URLField(blank=True, max_length=500)
    img = models.ImageField(verbose_name='Логотип соц.сети', blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('social', kwargs={'url': self.social_url})
    class Meta:
        verbose_name = 'Соц.сеть'
        verbose_name_plural = 'Соц.сети'