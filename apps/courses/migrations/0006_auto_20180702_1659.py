# Generated by Django 2.0.6 on 2018-07-02 16:59

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180629_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情'),
        ),
    ]
