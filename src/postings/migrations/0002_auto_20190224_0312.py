# Generated by Django 2.1.7 on 2019-02-24 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khassidapost',
            name='coverImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
