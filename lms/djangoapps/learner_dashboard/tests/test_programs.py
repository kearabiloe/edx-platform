"""
Tests for viewing the programs enrolled by a learner.
"""
import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from opaque_keys.edx import locator
import unittest
import ddt

from student.tests.factories import UserFactory
from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from xmodule.modulestore.tests.factories import CourseFactory
from student.models import CourseEnrollment
from common.test.utils import XssTestMixin
from mixins import LearnerDashboardConfigMixin


@unittest.skipUnless(settings.ROOT_URLCONF == 'lms.urls', 'Test only valid in lms')
@ddt.ddt
class TestProgramListing(ModuleStoreTestCase, XssTestMixin, LearnerDashboardConfigMixin):
    """
    Unit tests for getting the list of programs enrolled by a logged in user
    """
    PASSWORD = 'test'

    def setUp(self):
        """
        Add a student
        """
        super(TestProgramListing, self).setUp()
        self.student = UserFactory()
        self.student.set_password(self.PASSWORD)
        self.student.save()

        # Old Course
        old_course_location = locator.CourseLocator('Org0', 'Course0', 'Run0')
        course, enrollment = self._create_course_and_enrollment(old_course_location)
        enrollment.created = datetime.datetime(1900, 12, 31, 0, 0, 0, 0)
        enrollment.save()

        # New Course
        course_location = locator.CourseLocator('Org1', 'Course1', 'Run1')
        self.course, self.enrollment = self._create_course_and_enrollment(course_location)

    def _create_course_and_enrollment(self, course_location):
        """ Creates a course and associated enrollment. """
        course = CourseFactory.create(
            org=course_location.org,
            number=course_location.course,
            run=course_location.run
        )
        enrollment = CourseEnrollment.enroll(self.student, course.id)
        return course, enrollment

    def test_get_programs(self):
        self.create_learner_dashboard_config()
        self.client.login(username=self.student.username, password=self.PASSWORD)
        response = self.client.get(reverse("get_program_listing_view"))
        self.assertEqual(response.status_code, 200)

    def test_get_programs_dashboard_not_enabled(self):
        self.create_learner_dashboard_config(enable_learner_dashboard=False)
        self.client.login(username=self.student.username, password=self.PASSWORD)
        response = self.client.get(reverse("get_program_listing_view"))
        self.assertEqual(response.status_code, 404)
