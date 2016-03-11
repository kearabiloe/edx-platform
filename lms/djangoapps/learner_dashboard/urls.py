"""
Learner's Dashboard urls
"""

from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^programs', 'learner_dashboard.views.view_programs', name="get_program_listing_view")
)
