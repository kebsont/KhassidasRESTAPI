# Generated by Django 2.1.7 on 2019-02-24 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0002_auto_20190224_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='khassidapost',
            name='category',
            field=models.CharField(blank=True, default='All', max_length=120, null=True),
        ),
    ]
