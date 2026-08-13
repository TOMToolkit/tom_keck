from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from tom_keck.keck import KeckFacility
from tom_keck.models import KeckProfile
from tom_keck.templatetags.keck_extras import keck_profile_data


class TestApp(TestCase):
    """NOTE: to run these tests in your venv: python ./tom_keck/tests/run_tests.py"""

    def test_unittest(self):
        """Ensure the testing infrastructure is working."""
        self.assertTrue(True)


class TestKeckFacility(TestCase):

    def test_detail_url_name_resolves(self):
        """KeckFacility.detail_url_name must reverse to the mounted detail page --
        its namespace half is urls.py's app_name, derived from the AppConfig's name."""
        self.assertEqual(reverse(KeckFacility.detail_url_name), '/keck/')


class TestKeckProfileData(TestCase):

    def test_first_visit_creates_profile_and_full_context(self):
        """Regression: the first profile-page visit must render, not 500.

        The missing-profile branch used to return a context without keck_profile, so the
        partial's Edit link reversed with pk='' and raised NoReverseMatch on first visit.
        """
        user = User.objects.create_user(username='new_keck_user', password='s3cret')
        context = keck_profile_data(user)
        self.assertEqual(context['keck_profile'].user, user)
        self.assertIn('keck_profile_data', context)
        self.assertIn('keck_password', context)


class TestProfileUpdateViewAuth(TestCase):

    def test_anonymous_is_redirected_to_login(self):
        """Anonymous users must not be served a credentials form."""
        owner = User.objects.create_user(username='keck_owner', password='s3cret')
        profile, _ = KeckProfile.objects.get_or_create(user=owner)
        response = self.client.get(reverse('tom_keck:keck-profile-update', kwargs={'pk': profile.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_user_cannot_update_another_users_profile(self):
        """The queryset is owner-scoped, so someone else's profile pk is a 404."""
        owner = User.objects.create_user(username='keck_owner', password='s3cret')
        other = User.objects.create_user(username='keck_other', password='s3cret')
        profile, _ = KeckProfile.objects.get_or_create(user=owner)
        self.client.force_login(other)
        response = self.client.get(reverse('tom_keck:keck-profile-update', kwargs={'pk': profile.pk}))
        self.assertEqual(response.status_code, 404)
