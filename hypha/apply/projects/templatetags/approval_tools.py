from django import template

from ..permissions import has_permission

register = template.Library()


@register.simple_tag
def has_project_sow_form(project):
    return project.submission.page.specific.sow_forms.exists()


def user_has_approved(project, user):
    """Has the given User already approved the given Project"""
    return project.approvals.filter(by=user).exists()


@register.simple_tag
def user_can_send_for_approval(project, user):
    return user.is_apply_staff and project.can_send_for_approval


@register.simple_tag
def user_can_update_paf_approvers(project, user, request):
    permission, _ = has_permission('paf_approvers_update', user, object=project, raise_exception=False, request=request)
    return permission


@register.simple_tag
def user_can_assign_approvers_to_project(project, user, request):
    permission, _ = has_permission('paf_approvers_assign', user, object=project, raise_exception=False, request=request)
    return permission


@register.simple_tag
def user_can_update_paf_status(project, user, **kwargs):
    request = kwargs.get('request')
    if request:
        permission, _ = has_permission('paf_status_update', user, object=project, raise_exception=False, request=request)
        return permission
    return False


@register.simple_tag
def user_can_edit_project(project, user):
    return project.editable_by(user)
