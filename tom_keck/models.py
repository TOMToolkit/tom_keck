import logging

from django.db import models

from tom_common.models import EncryptableModelMixin, EncryptedProperty

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class KeckProfile(EncryptableModelMixin, models.Model):
    """User Profile for the TOMToolkit Keck Facility
    """
    keck_username = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Swift Username"
    )

    _keck_password = models.BinaryField(null=True, blank=True)
    keck_password = EncryptedProperty("_keck_password")
