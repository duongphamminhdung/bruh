from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    x = models.IntegerField()
    y = models.IntegerField()
    
    def __str__(self):
        return self.name

class Room(models.Model):
    room_id = models.IntegerField()
    order = models.IntegerField()
    p1 = Player()
    p2 = Player()
    p3 = Player()
    p4 = Player()

    def __str__(self):
        return str(self.room_id)
    
    class Meta:
        ordering = ('order', )

class lst(list):
    def __add__(self, *args, **kwargs):
        return lst(super().__add__(*args, **kwargs))
    