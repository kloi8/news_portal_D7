from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewDetail, NewsSearch, NewCreate, NewUpdate, NewDelete, subscriptions #IndexView
from django.views.decorators.cache import cache_page


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем новостям у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', cache_page(1)(NewsList.as_view()), name='news_list'),
   # pk — это первичный ключ новости, которая будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   # path('<int:pk>', cache_page(60*5)(NewDetail.as_view()), name='post_detail'),
   path('<int:pk>', NewDetail.as_view(), name='post_detail'),
   path('search/', NewsSearch.as_view()),
   path('create/', NewCreate.as_view(), name='post_create'),
   path('article/create/', NewCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', NewUpdate.as_view(), name='post_update'),
   path('article/<int:pk>/update/', NewUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', NewDelete.as_view(), name='post_delete'),
   path('article/<int:pk>/delete/', NewDelete.as_view(), name='post_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
   # path('index', IndexView.as_view()),
]