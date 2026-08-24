from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=64)
    native = models.CharField(max_length=64)
    bcp47 = models.CharField(max_length=16)
    group = models.CharField(max_length=64)
    is_phrasebook = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name} ({self.code})'


class Phrase(models.Model):
    slug = models.SlugField(max_length=64, primary_key=True)
    order = models.PositiveIntegerField(default=0)
    translations = models.JSONField(default=dict)
    translit = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.translations.get('en', self.slug)
