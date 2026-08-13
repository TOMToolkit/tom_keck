from django import template
from django.forms.models import model_to_dict

from tom_keck.models import KeckProfile

register = template.Library()


@register.inclusion_tag('tom_keck/partials/profile_keck.html')
def keck_profile_data(user) -> dict:
    """
    Returns the app specific user information as a dictionary to be used in the context of the above partial.
    """
    # get_or_create so a user who has never saved Keck info gets an empty profile on first
    # view, and every path returns the same fully-populated context. (A missing-profile
    # branch that returned only {'user': ...} left the partial's Edit link reversing with
    # pk='', which 500'd the profile page on its first visit.)
    keck_profile, _ = KeckProfile.objects.get_or_create(user=user)

    # keck_password is rendered separately via tom_common's revealable_password_input
    # partial, so exclude it from the auto-iteration loop. model_to_dict goes
    # through EncryptedModelField.value_from_object, which returns the REDACTED
    # placeholder string for security; the partial needs the actual plaintext,
    # which only direct attribute access provides.
    exclude_fields = ['user', 'id', 'keck_password']
    return {
        'user': user,
        'keck_profile': keck_profile,
        'keck_profile_data': model_to_dict(keck_profile, exclude=exclude_fields),
        'keck_password': keck_profile.keck_password,  # direct access → plaintext
    }
