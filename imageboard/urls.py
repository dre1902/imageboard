from django.urls import path

from . import views

app_name = 'imageboard'
urlpatterns = [
    path('<str:board_name>/', views.board_view, name='board_view'),
    path('<str:board_name>/thread/<int:post_num>', views.thread_view, name='thread_view')
]