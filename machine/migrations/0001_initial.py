# Generated by Django 2.1.2 on 2018-11-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csvFile', models.FileField(upload_to='', verbose_name='训练文件')),
                ('name', models.CharField(max_length=120)),
                ('imageFile', models.ImageField(upload_to='', verbose_name='产生文件')),
            ],
        ),
    ]
