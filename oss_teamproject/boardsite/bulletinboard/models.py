from django.db import models

class BulletinBoard(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목") # 글 제목
    contents = models.TextField(verbose_name="내용") # 글 내용
    username = models.ForeignKey('board.User', on_delete=models.CASCADE, verbose_name="글 작성자") # 글 작성자
    write_date = models.DateTimeField(auto_now_add=True, verbose_name="작성 날짜") # 작성된 날짜

    board_category = models.CharField(max_length = 50, default='Python', verbose_name="게시판 카테고리")   # 게시판 분류
    last_update = models.DateTimeField(auto_now = True, verbose_name="최근 수정된 날짜")    # 마지막 수정된 날짜
    view_count = models.PositiveIntegerField(default=0, verbose_name = '조회수')   # 글 조회수

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
# Create your models here.
