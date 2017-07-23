from django.db.models.signals import post_save
from django.dispatch import receiver

import requests

from rest_framework.response import Response

from jobonicusers.models import JobonicUser
from keys import SENDGRIDKEY


# sends the user an email after signup
@receiver(post_save, sender=JobonicUser)
def send_user_email(sender, instance, **kwargs):
    email = instance.email
    uuid = instance.uuid_info
    link = "https://jobonics.com/activate" + str(uuid) + "/" + email
    url = 'https://api.sendgrid.com/v3/mail/send'
    data = {"personalizations":
                [{"to": [{"email": email}]
                  }],
            "from": {"email": "support@jobonics.com"},
            "subject": "Welcome to Jobonics",
            "content": [{"type": "text/html", "value": "<h1>Welcome to Jobonics</h1><p>Thank you for joining this wonderful platform"
                                                       "Please follow this <a href='" + link + "'>link</a> to activate your account.</p>"}]
            }

    headers = {'Authorization': 'Bearer ' + SENDGRIDKEY,
               'Content-Type': 'application/json'
               }

    r = requests.post(url, json=data, headers=headers)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", r)
    return Response({
        "message": "Email sent",
        "data": r.text,
        "info": r.content
    })
