# Generated by Django 3.2 on 2021-05-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0038_delete_news_letters'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMAIL_LETTERS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
