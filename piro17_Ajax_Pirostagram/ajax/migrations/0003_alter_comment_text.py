# Generated by Django 4.0.6 on 2022-07-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0002_remove_comment_deleted_remove_comment_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=250, null=True, verbose_name='댓글 내용'),
        ),
    ]
