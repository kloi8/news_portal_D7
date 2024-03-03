from celery import shared_task
import datetime
from django.template.loader import render_to_string
from django.conf import settings
from news.models import Post, Subscription
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User



# @shared_task
# def hello():
#     time.sleep(10)
#     print("Hello, world!")
#
# @shared_task
# def printer(N):
#     for i in range(N):
#         time.sleep(1)
#         print(i+1)


@shared_task
def send_notifications_task(pk):
    instance = Post.objects.get(pk=pk)
    title = Post.title
    subscribers = Subscription.user
    emails = User.objects.filter(
        subscriptions__category__in=instance.postCategory.all()
    ).values_list('email', flat=True)

    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': Post.preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    subject = f'Новая статья в категории {instance.postCategory.all()}'

    text_content = (
        f'Новость: {instance.title}\n'
        f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Новость: {instance.title}<br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на статью</a>'
    )


    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
        msg.attach_alternative('html_content', 'text/html')
        msg.send()



@shared_task
def weekly_email_task():
        today = datetime.datetime.now()
        last_week = today - datetime.timedelta(days=7)
        posts = Post.objects.filter(dateCreation__gte=last_week)
        categories = set(posts.values_list('postCategory__name', flat=True))
        subscribers = set(Subscription.objects.filter(category__name__in=categories).values_list('user__email', flat=True))
        html_content = render_to_string(
            'daily_post.html',
            {
                'link': settings.SITE_URL,
                'posts': posts,

            }

        )
        msg = EmailMultiAlternatives(
            subject='Статьи за неделю',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=subscribers,
        )
        msg.attach_alternative(html_content, 'txt/html')
        msg.send()