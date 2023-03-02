from django.db import models

# Create your models here.
class Player(models.Model):
    def __init__(self, num, char):
        self.num = num
        self.char = char
    name = models.CharField(max_length=50)
    x = models.IntegerField()
    y = models.IntegerField()
    char_choices = [('A', 'A'), 
                    ('Z', 'Z'), 
                    ('U','U'), 
                    ('R','R'), 
                    ('E','E'), 
                    ('S','S'),
                    ]
    char = models.CharField(max_length=2, choices=char_choices, default = "A")
    def __str__(self):
        return self.name

class Room(models.Model):
    room_id = models.IntegerField()
    order = models.IntegerField()
    p1 = Player(1, 'A')
    p2 = Player(2, 'Z')
    p3 = Player(3, 'U')
    p4 = Player(4, 'R')

    def __str__(self):
        return str(self.room_id)
    
    class Meta:
        ordering = ('order', )

class lst(list):
    def __add__(self, *args, **kwargs):
        return lst(super().__add__(*args, **kwargs))
    