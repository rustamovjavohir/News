from django.urls import path
from news.views import (
    news_page,
    news_create_page,
    news_create,
    news_details_page,
    news_delete_page,
    news_delete, leave_comment)

app_name = 'news'
urlpatterns = [
    path('', news_page, name='news_page'),
    path('create_page/', news_create_page, name='news_create_page'),
    path('create/', news_create, name='news_create'),
    path('details/<int:pk>', news_details_page, name='news_details_page'),
    path('delete_page/<int:pk>', news_delete_page, name='news_delete_page'),
    path('delete/<int:pk>', news_delete, name='news_delete'),
    path('leave_comment/<int:post_id>', leave_comment, name='leave_comment'),
]
