from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 250)
    author = models.ForeignKey(User, default=1, on_delete=None)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def summary(self):
        return self.body[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")

    def __str__(self):
        return self.title
