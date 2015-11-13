from django.db import models


class Test(models.Model):
    """  """

    lala = models.CharField(blank=True, max_length=80)

    def __unicode__(self):
        return self.link