from tom_observations.facility import BaseRoboticObservationFacility, BaseRoboticObservationForm


class KeckFacilityForm(BaseRoboticObservationForm):
    pass


class KeckFacility(BaseRoboticObservationFacility):
    name = 'Keck'
    observation_types = [('OBSERVATION', 'Custom Observation')]

    def data_products(self):
        pass

    def get_form(self):
        pass

    def get_observation_status(self):
        pass

    def get_observation_url(self):
        pass

    def get_observing_sites(self):
        pass

    def get_terminal_observing_states(self):
        pass

    def submit_observation(self):
        pass

    def validate_observation(self):
        pass
