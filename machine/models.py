from django.db import models

# Create your models here.



class CsvModel(models.Model):
    csvFile = models.FileField(upload_to='csv',verbose_name="训练文件")
    name = models.CharField(max_length=120)
    imageFile = models.ImageField(upload_to='images', verbose_name="产生文件",null=True)
    class Meta:
        ordering = ('name',)