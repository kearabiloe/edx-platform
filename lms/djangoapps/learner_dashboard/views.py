"""
Handles requests for views, returning page frame
"""

import logging
from urlparse import urljoin

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import Http404

from edxmako.shortcuts import render_to_response
from openedx.core.djangoapps.programs.utils import get_programs_for_dashboard
from learner_dashboard.models import LearnerDashboardConfiguration
from student.views import get_course_enrollments


log = logging.getLogger(__name__)


@login_required
@ensure_csrf_cookie
def view_programs(requests):
    if not LearnerDashboardConfiguration.current().enable_learner_dashboard:
        raise Http404("learner dashboard not enabled")

    course_enrollments = list(get_course_enrollments(requests.user, None, []))

    # Get the programs by courses dictionary from the get_programs_for_dashboard function call
    programs_dict = get_programs_for_dashboard(
        requests.user,
        [enrollment.course_id for enrollment in course_enrollments])

    program_list = []
    # Extract all the programs from the dictionary above
    for programs_by_courses in programs_dict.values():
        for program in programs_by_courses:
            if program not in program_list:
                # Remove duplicates
                program['marketing_url'] = urljoin(
                    settings.MKTG_URLS.get('ROOT'),
                    'xseries' + '/{}'
                ).format(program['marketing_slug'])
                program_list.append(program)

    xseries_url = urljoin(settings.MKTG_URLS.get('ROOT'), 'xseries')

    return render_to_response('learner_dashboard/programs.html', {
        'programs': program_list,
        'xseries_url': xseries_url
    })
