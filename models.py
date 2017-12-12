from django.db import models

# Create your models here.

class Userinfo(models.Model):
    name = models.CharField(verbose_name='用户姓名',max_length=10)
    password = models.CharField(verbose_name='密码',max_length=10)

class Room(models.Model):
    title = models.CharField(verbose_name='会议室',max_length=10)
    num = models.IntegerField(verbose_name='会议室容量')

class Relationship(models.Model):
    date = models.DateField(verbose_name='预定日期')
    user = models.ForeignKey(verbose_name='用户',to='Userinfo')
    room = models.ForeignKey(verbose_name='会议室',to='Room')
    time_list = (
        (1, '8:00'),
        (2, '9:00'),
        (3, '10:00'),
        (4, '11:00'),
        (5, '12:00'),
        (6, '13:00'),
        (7, '14:00'),
        (8, '15:00'),
        (9, '16:00'),
        (10, '17:00'),
        (11, '18:00'),
        (12, '19:00'),
        (13, '20:00'),
    )
    time_select = models.IntegerField(verbose_name='预定时间段',choices=time_list)

    class Meta:
        unique_together = (
            ('date', 'room', 'time_select')
        )