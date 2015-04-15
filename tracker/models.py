from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    client = models.ForeignKey('Client')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = (
            ('client', 'code'),
            ('client', 'name'),
        )

    def __unicode__(self):
        return u'[%s] %s' % (self.client, self.name)


class Entry(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=100)
    project = models.ForeignKey('Project')

    class Meta:
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return u'{} [{} - {}]'.format(self.description, self.start, self.end)
