from django import template
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

from tom_keck.models import KeckProfile

register = template.Library()


@register.inclusion_tag('tom_keck/partials/profile_keck.html')
def keck_profile_data(user):
    """
    Returns the app specific user information as a dictionary to be used in the context of the above partial.
    """

    # keck_password is rendered separately via tom_common's revealable_password_input
    # partial, so exclude it from the auto-iteration loop. model_to_dict goes
    # through EncryptedModelField.value_from_object, which returns the REDACTED
    # placeholder string for security; the partial needs the actual plaintext,
    # which only direct attribute access provides.
    exclude_fields = ['user', 'id', 'keck_password']
    try:
        keck_profile_dict = model_to_dict(user.keckprofile, exclude=exclude_fields)
        profile_data = {
            'user': user,
            'keck_profile': user.keckprofile,
            'keck_profile_data': keck_profile_dict,
            'keck_password': user.keckprofile.keck_password,  # direct access → plaintext
        }
        return profile_data
    except KeckProfile.DoesNotExist:
        KeckProfile.objects.create(user=user)
        profile_data = {'user': user}
        return profile_data
