from django.core.mail import send_mail
from celery import shared_task 
from spam.models import Contact

@shared_task
def big_function():
    import time 
    time.sleep(10)
    
@shared_task
def send_product_news(title , price ):
    emails = [i.email for i in Contact.objects.all()]

    send_mail(
        'Py25 shop project', # title
        f'Привет загляни на наш сайт у нас вышел новый продукт {title} , у нее стоимость всего лиж {price}', # body
        'githubforsam@gmail.com', # from
        emails # to
    )