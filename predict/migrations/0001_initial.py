# Generated by Django 3.2.12 on 2022-04-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.FloatField()),
                ('ap_hi', models.IntegerField()),
                ('ap_lo', models.IntegerField()),
                ('cholesterol', models.IntegerField()),
                ('gluc', models.IntegerField()),
                ('smoke', models.BooleanField()),
                ('alco', models.BooleanField()),
                ('active', models.BooleanField()),
                ('years', models.IntegerField()),
            ],
        ),
    ]