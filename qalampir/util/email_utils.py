import threading

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from accout.models import VerifyToken
from qalampir.settings import EMAIL_HOST_USER
from qalampir.util.base_utils import unique_code


class SendEmailAsync(threading.Thread):
    pass


class SendHtmlEmailAsync(threading.Thread):
    def __init__(self, from_email=None, to=None, subject=None, html_content=None):
        super(SendHtmlEmailAsync, self).__init__()
        self.from_email = from_email
        self.to = to
        self.subject = subject
        self.html_content = html_content
        self.email_type = 'html'

    def run(self) -> None:
        email = EmailMessage(
            subject=self.subject,
            body=self.html_content,
            from_email=self.from_email,
            to=self.to)
        email.content_subtype = self.email_type
        email.send()


def send_verification_token(template_name, subject, user: User) -> None:
    code = unique_code()
    VerifyToken(token=code, auth_user=user).save()
    content = render_to_string(template_name, context={'token': code})
    message = SendHtmlEmailAsync(from_email=EMAIL_HOST_USER, to=[user.email, ], subject=subject, html_content=content)
    message.start()
