# Generated by Django 4.0.6 on 2022-07-27 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='게시글 이름')),
                ('content', models.TextField(verbose_name='게시글 내용')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True, verbose_name='댓글 내용')),
                ('like', models.BooleanField(default=False, verbose_name='좋아요')),
                ('deleted', models.BooleanField(default=False, verbose_name='삭제 여부')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ajax.post')),
            ],
        ),
    ]
