from django.urls import path
from webapp.views import index_view, about_view, article_create_view, task1_view

urlpatterns = [
    path('', index_view),
    path('about/', about_view),
    path('articles/add/',article_create_view),
    path('task1/', task1_view)
]
