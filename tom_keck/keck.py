from __future__ import annotations

from crispy_forms.layout import Layout
from django import forms

from tom_observations.facility import BaseRoboticObservationFacility, BaseRoboticObservationForm

from tom_keck.apps import TomKeckConfig


class KeckFacilityForm(BaseRoboticObservationForm):
    exposure_time = forms.IntegerField()
    exposure_count = forms.IntegerField()

    def layout(self):
        return Layout(
            'exposure_time',
            'exposure_count'
        )


class KeckFacility(BaseRoboticObservationFacility):
    name = 'Keck'
    # Detail page linked from the navbar "Facilities" menu. The AppConfig's name is the
    # single source of truth for the namespace; guarded by test_detail_url_name_resolves.
    detail_url_name = f'{TomKeckConfig.name}:facility-detail'  # 'tom_keck:facility-detail'
    observation_types: list[tuple[str, str]] = [
        ('OBSERVATION', 'Custom Observation')
    ]

    observation_forms: dict[str, type[BaseRoboticObservationForm]] = {
        'OBSERVATION': KeckFacilityForm,
    }

    def data_products(self):
        pass

    def get_form(self, observation_type: str | None) -> type[BaseRoboticObservationForm]:
        """Return the observation form class for ``observation_type``.
        """
        if observation_type is None:
            return KeckFacilityForm
        return self.observation_forms.get(observation_type, KeckFacilityForm)

    def get_observation_status(self):
        pass

    def get_observation_url(self):
        pass

    def get_observing_sites(self) -> dict[str, dict]:
        """Return the facility's observing site(s) for the visibility and airmass planner.

        From Keck Telescope and Facility Instrument Guide:
        Observatory location: longitude: 155° 28.4' W
                              latitude: 19° 49.6' N
                              altitude: 4123 meter
        """
        keck_location_params = {
            'Mauna Kea': {
                'sitecode': 'keck',
                'latitude': 19.8267,
                'longitude': -155.4733,
                'elevation': 4123,
            }
        }
        return keck_location_params

    def get_terminal_observing_states(self):
        pass

    def submit_observation(self):
        pass

    def validate_observation(self):
        pass
