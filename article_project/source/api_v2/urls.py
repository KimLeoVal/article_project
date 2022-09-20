from django.urls import path

from .views import ArticleView

app_name='api_v2'
urlpatterns=[
    path('article/',ArticleView.as_view(),name='ArticleView'),
    path('article/<int:pk>/',ArticleView.as_view(),name='ArticleView'),
    # path('article/create/',ArticleCreateView.as_view(),name='ArticleCreateView'),
    # path('article/<int:pk>/update/',ArticleUpdateView.as_view(),name='ArticleUpdateView'),
    # path('article/<int:pk>/delete/',ArticleDeleteView.as_view(),name='ArticleDeleteView')
]
