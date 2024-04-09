# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import post_save, m2m_changed
# from django.dispatch import receiver
# from django.template.loader import render_to_string
#
# from .models import PostCategory
# from django.conf import settings
# from tasks import send_notifications
#
#
# def send_notifications(preview, pk, title, subscribers):
#     html_context = render_to_string(
#         'post_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}',
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#
#     msg.attach_alternative('html_content', 'text/html')
#     msg.send()
#
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def post_created(instance, sender, **kwargs):
#     # if kwargs['action'] != 'post_add':
#     if kwargs['action'] == 'post_add':
#         send_notifications.delay(instance.pk)
#
#     emails = User.objects.filter(
#         subscriptions__category__in=instance.postCategory.all()
#     ).values_list('email', flat=True)
#
#     subject = f'Новая статья в категории {instance.postCategory.all()}'
#
#     text_content = (
#         f'Новость: {instance.title}\n'
#         f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Новость: {instance.title}<br>'
#         f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
#         f'Ссылка на статью</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()