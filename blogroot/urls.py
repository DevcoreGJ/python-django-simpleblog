from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView
urlpatterns = [
    #path('', views.home, name="home") old type of url
    path('', HomeView.as_view(), name="home"),
    #pk = primary key, the url will autogen a new page based n int
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),
]
