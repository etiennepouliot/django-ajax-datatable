# Generated by Django 3.0.8 on 2020-09-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_custompk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='tags',
            field=models.ManyToManyField(to='backend.Tag'),
        ),
    ]
