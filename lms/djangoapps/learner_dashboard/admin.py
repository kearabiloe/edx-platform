""" Admin site bindings for learner dashboard app. """

from django.contrib import admin

from learner_dashboard.models import LearnerDashboardConfiguration
from config_models.admin import ConfigurationModelAdmin

admin.site.register(LearnerDashboardConfiguration, ConfigurationModelAdmin)
