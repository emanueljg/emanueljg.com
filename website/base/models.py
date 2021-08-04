from django.db import models
from django.utils import timezone
from bs4 import BeautifulSoup


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    _snippet = models.TextField(blank=True)
    _date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def date_posted(self):
        return self._date_posted.strftime(r'%Y-%m-%dT%H:%M:%SZ')
    
    @property
    def snippet(self):
        return self._snippet or BeautifulSoup(self.content, 'html.parser').p.string

    @property
    def relative_url(self):
        return f'../../post/{self.pk}'

    

