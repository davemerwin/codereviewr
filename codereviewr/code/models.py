from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Code(models.Model):
    """
    Core code model for code snippets
    """
    title = models.CharField(max_length=200)
    code = models.TextField(help_text="")
    author = models.ForeignKey(User)
    description = models.TextField(blank=True)
    dependencies = models.CharField(blank=True, max_length=255)
    # language ... get from Pygments
    version = models.CharField(blank=True, max_length=100)
    is_public = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(blank=True, default=datetime.now)

    def __unicode__(self):
        return "%s by %s" % (self.title, self.author.get_full_name())

    class Admin:
        list_display = ('title','author','is_public','created')
