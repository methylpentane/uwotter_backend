# Generated by Django 3.2.7 on 2021-09-16 02:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('voice', models.BinaryField(verbose_name='ウオート')),
                ('like_num', models.IntegerField(default=0, verbose_name='いいね数')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.myuser', verbose_name='投稿者')),
                ('like', models.ManyToManyField(related_name='like_people', to='user.MyUser', verbose_name='いいね')),
                ('tag', models.ManyToManyField(to='tag.Tag', verbose_name='タグ')),
            ],
            options={
                'db_table': 'voice',
            },
        ),
    ]
