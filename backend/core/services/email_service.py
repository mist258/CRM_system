import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from configs.celery import app
from core.services.jwt_service import JWTService, RecoveryToken

from .jwt_service import ActivateToken


class EmailService:

    @staticmethod
    @app.task
    def __send_email(to: str, template_name: str, context: {}, subject=''):

        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject=subject, from_email=os.environ.get("EMAIL_HOST_USER"), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def activate(cls, user):
        token = JWTService.generate_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email.delay(user.email,
                         "activate.html",
                         {
                             'first_name': user.profile.name,
                             'surname': user.profile.surname,
                             'url': url,
                         },
                         'Activate email')

    @classmethod
    def recovery_password(cls, user):
        token = JWTService.generate_token(user, RecoveryToken)
        url = f'http://localhost:3000/recovery_password/{token}'
        cls.__send_email.delay(user.email,
                         "recovery.html",
                         {
                             'first_name': user.profile.name,
                             'surname': user.profile.surname,
                             'url': url,
                         },
                         'Recovery password')