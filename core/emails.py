from djoser import utils
from djoser.conf import settings
from django.contrib.auth.tokens import default_token_generator
from djoser.email import ConfirmationEmail

class CustomConfirmationEmail(ConfirmationEmail):
    template_name = 'email/confirmation.html'

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.CONFIRMATION_URL.format(**context)
        return context