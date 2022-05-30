from django.db import models

class User(models.Model):
    u_id = models.CharField(max_length=40, unique=True, verbose_name='사용자 아이디')
    u_pw = models.CharField(max_length=100, verbose_name='사용자 비밀번호')
    u_name = models.CharField(max_length=20, unique=True, verbose_name='사용자 이름')
    u_phone = models.CharField(max_length=40, unique=True, verbose_name='사용자 번호')
    u_register_date = models.DateTimeField(auto_now_add=True, verbose_name='사용자 계정 생성 시간')
    def __str__(self):
        return self.u_name

    class Meta:
        db_table = 'user'
        verbose_name = '유저 정보'
        verbose_name_plural = '유저 정보'

