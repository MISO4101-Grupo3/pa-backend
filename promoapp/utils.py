import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
import sendgrid
from sendgrid.helpers.mail import *
from django.conf import settings

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)


#https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error/42334357#42334357
def send_email(to, subject, message, sender_email):
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    from_email = Email(sender_email)
    to_email = Email(to)
    content = Content("text/plain", message)
    sg_mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=sg_mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)