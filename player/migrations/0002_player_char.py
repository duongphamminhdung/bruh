# Generated by Django 4.0.4 on 2023-03-02 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='char',
            field=models.CharField(choices=[('A', 'A'), ('Z', 'Z'), ('U', 'U'), ('R', 'R'), ('E', 'E'), ('S', 'S')], default='A', max_length=2),
        ),
    ]