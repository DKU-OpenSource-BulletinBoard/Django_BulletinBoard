from django import forms
from .models import BulletinBoard
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class BulletinWriteForm(forms.ModelForm):
    title = forms.CharField(
        label = '게시글 제목',
        widget = forms.TextInput(
            attrs = {
                'placehorder': '해당 게시글의 제목을 입력하세요'
            }),
        required = True,
        )
    contents = SummernoteTextField()

    # 게시판 카테고리 종류
    bulletin_options = (
        ('Sports', '스포츠 게시판'),
        ('Politics', '정치 게시판'),
        ('Free', '자유 게시판 ')
    )

    field_order = [
        'title',
        'board_category',
        'contents'
    ]

    board_category = forms.ChoiceField (
        label = '게시판 종류 선택',
        widget = forms.Select(),
        choices = bulletin_options
    )

    class Meta:
        model = BulletinBoard
        fields = [
            'title',
            'contents',
            'board_category'
        ]
        widgets = {
            'contents' : SummernoteWidget()
        }

    def clean(self):
        cleaning = super().clean()

        title = cleaning.get('title', '')
        contents = cleaning.get('contents', '')
        board_category = cleaning.get('board_category', 'Free')

        if  contents == '':
            self.add_error('contents', '글 내용에 해당하는 필드를 입력하세요.')
        elif title == '':
            self.add_error('title', '글 제목은 빈 칸이 될 수 없습니다.')
        else:
            self.title = title
            self.contents = contents
            self.board_category = board_category

