from learner_dashboard.models import LearnerDashboardConfiguration


class LearnerDashboardConfigMixin(object):
    """Utilities for working with Learner's Dashboard configuration during testing."""

    DEFAULTS = {
        'enabled': True,
        'enable_learner_dashboard': True
    }

    def create_learner_dashboard_config(self, **kwargs):
        """Creates a new LearnerDashboardConfiguration with DEFAULTS, updated with any provided overrides."""
        fields = dict(self.DEFAULTS, **kwargs)
        LearnerDashboardConfiguration(**fields).save()
        return LearnerDashboardConfiguration.current()
