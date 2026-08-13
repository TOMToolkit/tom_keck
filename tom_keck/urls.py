from django.urls import path
from django.views.generic import TemplateView

from .apps import TomKeckConfig
from .views import ProfileUpdateView


# app_name supplies the '<namespace>:' half of this app's URL names, e.g. {% url 'tom_keck:<name>' %}.
# Deriving app_name from the AppConfig.name means the namespace and the package name can never disagree.
app_name = TomKeckConfig.name  # the AppConfig.name is thus the single-source of 'truth'

urlpatterns = [
    # stub detail page for the Keck facility, linked from the navbar "Facilities" menu
    # (declared as KeckFacility.detail_url_name in keck.py)
    path('', TemplateView.as_view(template_name='tom_keck/facility_detail.html'), name='facility-detail'),
    path('users/<int:pk>/update/', ProfileUpdateView.as_view(), name='keck-profile-update'),
]
