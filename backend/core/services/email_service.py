import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.services.jwt_service import JWTService

from .jwt_service import ActivateToken


class EmailService:

    @staticmethod
    def __send_email(to: str, template_name: str, context: {}, subject=''):

        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject=subject, from_email=os.environ.get("EMAIL_HOST_USER"), to=[to])
        msg.attach_alternative(html_content, "text/html")

    @classmethod
    def activate(cls, user):
        token = JWTService.generate_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email(user.email,
                         "activate.html",
                         {
                             'first_name': user.profile.name,
                             'surname': user.profile.surname,
                             'url': url,
                         },
                         'Activate email'
                         )

