# Generated by Django 3.2.4 on 2021-09-03 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('detail', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('dateListed', models.DateTimeField(default=django.utils.timezone.now)),
                ('isActive', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='')),
                ('startPrice', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AuctionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('timePlaced', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
