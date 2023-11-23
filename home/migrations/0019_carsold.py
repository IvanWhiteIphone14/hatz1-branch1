# Generated by Django 4.2.7 on 2023-11-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_car_main_photo_remove_carphoto_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('price_month', models.CharField(default='N/A', max_length=10)),
                ('shorter_info', models.TextField(default='N/A')),
                ('short_info', models.TextField(default='short info')),
                ('traction', models.TextField(default='N/A')),
                ('gearbox', models.TextField(default='Automatic')),
                ('engine', models.TextField(default='N/A')),
                ('stock', models.TextField(default='N/A')),
                ('vin', models.TextField(default='N/A')),
                ('mileage', models.TextField(default='N/A')),
                ('body_color', models.TextField(default='N/A')),
                ('interior_color', models.TextField(default='N/A')),
                ('year', models.IntegerField()),
                ('photo_test_main', models.TextField(default='N/A')),
                ('video_photo', models.TextField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/1024px-YouTube_full-color_icon_%282017%29.svg.png')),
                ('video_link', models.TextField(default='<iframe width="1029" height="579" src="https://www.youtube.com/embed/BcJN9JGaYFQ" title="1977 CHEVROLET K20" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')),
            ],
        ),
    ]