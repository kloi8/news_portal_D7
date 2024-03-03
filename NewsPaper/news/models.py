from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.core.validators import MinValueValidator


# Описание моделей и что в них должно быть (+связи между моделями)
class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.authorUser.username}'

    def update_rating(self): # суммарный рейтинг всех комментариев к статьям
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        # суммарный рейтинг всех комментариев самого автора
        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        # суммарный рейтинг каждой статьи автора умноженный на 3
        self.ratingAuthor = pRat * 3 + cRat
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')


    def __str__(self):
        return f'{self.name}'

NEWS = 'NW'
ARTICLE = 'AR'

CATEGORY_CHOICES = [
        (NEWS, 'Новости'),
        (ARTICLE, 'Статья')
    ]
class Post(models.Model):
    objects = None
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=NEWS) #Выбор статьи или новости
    dateCreation = models.DateTimeField(auto_now_add=True) #Дата и время создания
    postCategory = models.ManyToManyField(Category, through='PostCategory') #Доп связь с категориями
    title = models.CharField(max_length=128) #Заголовок
    text = models.TextField() #текст
    rating = models.SmallIntegerField(default=0) #Рейтинг


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...' #Превью статьи в 124 символа

    def __str__(self):
        return f'{self.title.title()}: {self.dateCreation}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE) #чтобы была возможность комментировать не только авторам но и всем юзерам
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )