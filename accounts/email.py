from djoser import email
from django.conf import settings
from django.core.mail import send_mail


class CustomPasswordResetEmail(email.PasswordResetEmail):
    def send(self, to, *args, **kwargs):
        context = self.get_context_data()

        subject = 'Password Reset'
        message = f"Hello {context['user'].username},\n\n" \
                  f"You're receiving this email because you requested a password" \
                  f"reset for your user account at {context['site_name']}.\n\n"  \
                  f"Please go to the following page and choose a new password:\n" \
                  f"{context['url']}\n\n" \
                  f"Your username, in case you’ve forgotten: {context['user'].username}\n\n" \
                  f"Thanks for using our site!\n" \
                  f"The {context['site_name']} team"

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, to)


class CustomActivationEmail(email.ActivationEmail):
    def send(self, to, *args, **kwargs):
        context = self.get_context_data()

        subject = "Activation Account "
        message = f"Wassap Hello {context['user'].username},\n\n" \
                  f"You're receiving this email because you should to" \
                  f"activate your user account at {context['site_name']}.\n\n" \
                  f"Please go to the following page:\n" \
                  f"n{context['url']}\n\n" \
                  f"Thanks for using our site!\n" \
                  f"The {context['site_name']} team"

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, to)
