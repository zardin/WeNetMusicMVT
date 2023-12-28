from django.db import models

class Music(models.Model):
    MusicId = models.IntegerField()
    MusicName = models.CharField(max_length=50)
    ProposedBy = models.CharField(max_length=50)
    DateAdded = models.CharField(max_length=50)
    Description = models.CharField(max_length=500)
    MusicFile = models.FileField(upload_to='.')

    def __str__(self):
        return self.MusicName
