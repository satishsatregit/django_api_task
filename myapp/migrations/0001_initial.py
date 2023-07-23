# Generated by Django 4.2.3 on 2023-07-23 09:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=100, validators=[django.core.validators.MinValueValidator(limit_value=2)])),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('other_relevent_details', models.TextField()),
            ],
            options={
                'db_table': 'Bogpost',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.CharField(max_length=100, validators=[django.core.validators.MinValueValidator(limit_value=2)])),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('other_relevant_details', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_id', models.CharField(max_length=100)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.blogpost')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
            options={
                'db_table': 'like',
            },
        ),
    ]
