from django.urls import path
from webapp.views import index_view, about_view, article_create_view, task2_view, task1_view, task3_view, task6_view

urlpatterns = [
    path('', index_view),
    path('about/', about_view),
    path('articles/add/',article_create_view),

    path('tasks2/', task2_view),
    path('task1/', task1_view),
    path('task3/', task3_view),
    path('task6/', task6_view),
]
