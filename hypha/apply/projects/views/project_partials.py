from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from hypha.apply.activity.services import (
    get_related_actions_for_user,
)

from ..models.project import Project


@login_required
@require_GET
def partial_project_activities(request, pk):
    project = get_object_or_404(Project, pk=pk)
    ctx = {
        'actions': get_related_actions_for_user(project, request.user)
    }
    return render(request, 'activity/include/action_list.html', ctx)
