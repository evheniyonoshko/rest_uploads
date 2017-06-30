from __future__ import unicode_literals

from django.db import models


class Upload(models.Model):
    owner = models.ForeignKey('auth.User', related_name='uploads')
    author = models.EmailField(u"Email", max_length=254)
    key =  models.CharField('Key', max_length=20, 
                            blank=True, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    file = models.FileField(u"File", upload_to='files')
    description = models.CharField('Description', max_length=128,
                                    blank=True, null=True)

    def __str__(self):
        return self.key

    class Meta:
        ordering = ('uploaded',)
