# Generated by Django 4.2.3 on 2023-07-25 19:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djangoProjectTravel.photos.models
import djangoProjectTravel.photos.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destination', '0002_alter_destination_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='destination_photos/', validators=[djangoProjectTravel.photos.validators.validate_image_less_than_5mb])),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('publication_date', models.DateField(auto_now=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='destination.destination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(djangoProjectTravel.photos.models.StrFromFieldsMixin, models.Model),
        ),
    ]