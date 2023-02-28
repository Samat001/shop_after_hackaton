from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Py25 shop project', # title
        f'http://localhost:8000/api/v1/account/activate/{code}', # body
        'githubforsam@gmail.com', # from
        [email] # to
    )


def send_reset_password_code(email, code):
    send_mail(
        'Py25 shop project', # title
        f'привет что бы сбрость пароль тебе нужно знать этот код = {code}', # body
        'githubforsam@gmail.com', # from
        [email] # to
    )