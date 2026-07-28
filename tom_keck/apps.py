from django.apps import AppConfig
from django.urls import path, include


class TomKeckConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tom_keck'  # python path to the application, like 'django.contrib.admin'
    url_prefix = 'keck'  # URL path prefix for this app's pages: HOST:PORT/keck/... (see include_url_paths())

    # The following methods are TOMToolkit integration points

    def include_url_paths(self):
        """
        Integration point for adding URL patterns to the Tom Common URL configuration.
        This method should return a list of URL patterns to be included in the main URL configuration.

        Note: url_prefix only affects the path; the URL namespace remains self.label ('tom_keck'),
        so reverses like 'tom_keck:facility-index' are unaffected.
        """
        urlpatterns = [
            path(f'{self.url_prefix}/', include(f'{self.name}.urls', namespace=f'{self.label}'))
        ]
        return urlpatterns

    def observation_facilities(self):
        """
        Integration point for including this app's observation facilities in the TOM.
        Facility classes listed will be among those returned by
        ``tom_observations.facility.get_service_classes()``.

        This method should return a list of dictionaries, each with:
         - a `class` key giving the dot separated path to a Facility class.
         - an optional `url` key giving the namespaced URL name of the facility's landing page.

        If the optional `url` key is given, the Facility will appear in the navbar
        "Facilities" menu). Omit `url` for a facility with no landing page.
        """
        facilities = [
            {'class': f'{self.name}.keck.KeckFacility',
             'url': f'{self.label}:facility-index'},
        ]
        return facilities

    def profile_details(self):
        """
        Integration point for adding items to the user profile page.

        This method should return a list of dictionaries that include a `partial` key pointing to the path of the html
        profile partial. The `context` key should point to the dot separated string path to the templatetag that will
        return a dictionary containing new context for the accompanying partial.
        Typically, this partial will be a bootstrap card displaying some app specific user data.
        """
        return [{'partial': f'{self.name}/partials/profile_keck.html',
                 'context': f'{self.name}.templatetags.keck_extras.keck_profile_data'}]
