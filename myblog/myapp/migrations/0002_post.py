# Generated by Django 5.2.1 on 2025-05-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_date', models.DateField()),
                ('image', models.ImageField(upload_to='static/')),
                ('paragraph', models.TextField(max_length=100)),
            ],
        ),
    ]
