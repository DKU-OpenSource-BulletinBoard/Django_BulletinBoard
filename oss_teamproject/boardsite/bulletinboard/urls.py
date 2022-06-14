from django.urls import path
from . import views

app_name = 'bulletin_board'
urlpatterns = [
    path('', views.board_view, name='board_view'),
    path('write', views.write, name='write'),
    path('detail/<int:pk>/', views.bulletin_detail, name="bulletin_detail"),

]