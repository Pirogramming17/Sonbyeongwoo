# Generated by Django 4.0.6 on 2022-07-15 20:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('액션', '액션'), ('범죄', '범죄'), ('SF', 'SF'), ('로맨스', '로맨스'), ('코미디', '코미디'), ('공포', '공포')], max_length=4, null=True, verbose_name='장르'),
        ),
        migrations.AlterField(
            model_name='post',
            name='star',
            field=models.FloatField(help_text='value 0 to 5', validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='별점'),
        ),
    ]
