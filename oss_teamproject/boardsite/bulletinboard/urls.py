from django.urls import path
from . import views

app_name = 'bulletin_board'
urlpatterns = [
    path('', views.board_view, name='board_view')
]