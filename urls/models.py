from django.db import models
from django.utils.crypto import get_random_string

class URL(models.Model):
    Full_url = models.URLField()
    name = models.CharField(max_length=255)
    shorturl = models.CharField(max_length=5, unique=True, primary_key=True, editable=False)


    def save(self, *args, **kwargs):
        # Generate a unique 5-letter code
        if self.shorturl is None:
            while True:
                shorturl = get_random_string(length=5)
                if not URL.objects.filter(shorturl=shorturl).exists():
                    self.shorturl = shorturl
                    break

        super(URL, self).save(*args, **kwargs)
