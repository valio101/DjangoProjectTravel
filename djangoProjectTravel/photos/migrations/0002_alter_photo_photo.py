# Generated by Django 4.2.3 on 2023-07-26 02:14

from django.db import migrations, models
import djangoProjectTravel.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='destination_photos/', validators=[djangoProjectTravel.photos.validators.validate_image_less_than_5mb]),
        ),
    ]