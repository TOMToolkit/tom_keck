import logging

from django.contrib.auth.models import User
from django.db import models

from tom_common.encryption import EncryptedModelField


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class KeckProfile(models.Model):
    """User Profile for the TOMToolkit Keck Facility
    """
    # connect this Profile to it's User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    keck_username = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Keck Username"
    )
    keck_password = EncryptedModelField(null=True, blank=True)

