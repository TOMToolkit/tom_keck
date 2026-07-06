from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from tom_keck.models import KeckProfile


class ProfileUpdateView(UpdateView):
    """
    View that handles updating of a user's ``KeckProfile``.

    The Keck Facility has a ``KeckProfile`` model (see ``models.py``). This view updates
    the properties of that model.

    The ``KeckProfile`` properties are displayed by the ``keck_user_profile.html`` template.
    This typically happens on the on the User Profile page via the ``show_app_profiles``
    inclusion tag (see ``tom_base/tom_common/templates/tom_common/user_profile.html`` and
    ``tom_base/tom_common/templatetags/user_extras.py::show_app_profiles``).
    """
    model = KeckProfile
    template_name = 'tom_keck/update_profile.html'
    fields = ['keck_username', 'keck_password']  # required by ModelFormMixin, a base class of this ProfileUpdateView

    def get_success_url(self):
        return reverse_lazy('user-profile')  # back to the TOMToolkit user-profile
