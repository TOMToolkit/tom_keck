from django.urls import path
from django.views.generic import TemplateView

from .views import ProfileUpdateView


app_name = 'tom_keck'

urlpatterns = [
    # stub landing page for the Keck facility, linked from the navbar "Facilities" menu
    # (see TomKeckConfig.observation_facilities())
    path('', TemplateView.as_view(template_name='tom_keck/facility_index.html'), name='facility-index'),
    path('users/<int:pk>/update/', ProfileUpdateView.as_view(), name='keck-profile-update'),
]
