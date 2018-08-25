# Generated by Django 2.1 on 2018-08-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_gamecontentdocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('license', models.TextField()),
                ('author', models.TextField()),
                ('organization', models.TextField()),
                ('version', models.TextField()),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='GameContentDocument',
        ),
    ]
