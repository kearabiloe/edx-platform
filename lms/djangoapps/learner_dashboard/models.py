"""Models for Learner's Dashboard"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from config_models.models import ConfigurationModel


class LearnerDashboardConfiguration(ConfigurationModel):
    """
    Manages configuration for various aspects of the learner's dashboard
    """

    enable_learner_dashboard = models.BooleanField(
        verbose_name=_("Enable Learner Dashboard Access"),
        default=False
    )

    @property
    def is_learner_dashboard_enabled(self):
        """
        Indicates whether LMS dashboard for learners is enabled
        """
        return self.enabled and self.enable_student_dashboard
