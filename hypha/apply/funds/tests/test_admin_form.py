import factory
from django.test import TestCase

from hypha.apply.determinations.tests.factories import DeterminationFormFactory
from hypha.apply.funds.models import FundType
from hypha.apply.projects.tests.factories import (
    ProjectApprovalFormFactory,
    ProjectSOWFormFactory,
)
from hypha.apply.review.tests.factories import ReviewFormFactory

from .factories import ApplicationFormFactory, FundTypeFactory, workflow_for_stages


def formset_base(field, total, delete, factory, same=False, form_stage_info=None):
    base_data = {
        f'{field}-TOTAL_FORMS': total + delete,
        f'{field}-INITIAL_FORMS': 0,
    }

    required_forms = total + delete

    if not same:
        application_forms = factory.create_batch(required_forms)
    else:
        application_forms = [factory()] * required_forms

    deleted = 0
    for i, form in enumerate(application_forms):
        should_delete = deleted < delete
        base_data.update({
            f'{field}-{i}-form': form.id,
            f'{field}-{i}-ORDER': i,
            f'{field}-{i}-DELETE': should_delete,
        })
        if form_stage_info:
            # form_stage_info contains stage number for selected application forms
            stage = form_stage_info[i]
            base_data[f'{field}-{i}-stage'] = stage
        deleted += 1

    return base_data


def form_data(num_appl_forms=0, num_review_forms=0, num_determination_forms=0, num_external_review_forms=0, num_project_approval_form=0, num_project_sow_form=0, delete=0, stages=1, same_forms=False, form_stage_info=None):
    if form_stage_info is None:
        form_stage_info = [1]
    form_data = formset_base(
        'forms', num_appl_forms, delete, same=same_forms, factory=ApplicationFormFactory,
        form_stage_info=form_stage_info)
    review_form_data = formset_base('review_forms', num_review_forms, False, same=same_forms, factory=ReviewFormFactory)
    external_review_form_data = formset_base('external_review_forms', num_external_review_forms, True, same=same_forms, factory=ReviewFormFactory)
    determination_form_data = formset_base('determination_forms', num_determination_forms, False, same=same_forms, factory=DeterminationFormFactory)
    project_approval_form_data = formset_base('approval_forms', num_project_approval_form, False, same=same_forms, factory=ProjectApprovalFormFactory)
    project_sow_form_data = formset_base('sow_forms', num_project_sow_form, False, same=same_forms, factory=ProjectSOWFormFactory)

    form_data.update(review_form_data)
    form_data.update(external_review_form_data)
    form_data.update(determination_form_data)
    form_data.update(project_approval_form_data)
    form_data.update(project_sow_form_data)

    fund_data = factory.build(dict, FACTORY_CLASS=FundTypeFactory)
    fund_data['workflow_name'] = workflow_for_stages(stages)

    form_data.update(fund_data)
    return form_data


class TestWorkflowFormAdminForm(TestCase):

    def submit_data(self, data):
        form_class = FundType.get_edit_handler().get_form_class()
        return form_class(data=data)

    def test_doesnt_validates_with_no_form(self):
        form = self.submit_data(form_data())
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors['__all__'])

    def test_validates_with_one_form_one_stage(self):
        form = self.submit_data(form_data(1, 1, 1, 0, 1))
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_validates_with_one_form_one_stage_with_deleted(self):
        form = self.submit_data(form_data(1, 1, 1, 0, 1, delete=1, form_stage_info=[2, 1]))
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_doesnt_validates_with_two_forms_one_stage(self):
        form = self.submit_data(form_data(2, 2, 2, 0, 1, form_stage_info=[1, 2]))
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors['__all__'])
        formset_errors = form.formsets['forms'].errors
        # First form is ok
        self.assertFalse(formset_errors[0])
        # second form is too many
        self.assertTrue(formset_errors[1]['form'])

    def test_can_save_two_forms(self):
        form = self.submit_data(form_data(2, 2, 2, 0, 1, stages=2, form_stage_info=[1, 2]))
        self.assertTrue(form.is_valid())

    def test_can_save_multiple_forms_stage_two(self):
        form = self.submit_data(form_data(3, 2, 2, 0, 1, stages=2, form_stage_info=[1, 2, 2]))
        self.assertTrue(form.is_valid())

    def test_doesnt_validates_with_two_first_stage_forms_in_two_stage(self):
        form = self.submit_data(form_data(2, 2, 2, 0, 1, stages=2, form_stage_info=[1, 1]))
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors['__all__'])

    def test_validate_external_review_form(self):
        form = self.submit_data(form_data(1, 1, 1, num_external_review_forms=1, num_project_approval_form=1, stages=1))
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_validates_without_external_review_form(self):
        form = self.submit_data(form_data(1, 1, 1, num_external_review_forms=0, num_project_approval_form=1, stages=1))
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_doesnt_validates_with_multiple_external_review_form(self):
        form = self.submit_data(form_data(1, 1, 1, num_external_review_forms=2, num_project_approval_form=1, stages=1))
        self.assertFalse(form.is_valid(), form.errors.as_text())

    def test_validate_project_approval_form(self):
        form = self.submit_data(form_data(1, 1, 1, 0, num_project_approval_form=1, stages=1))
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_does_validates_without_project_approval_form(self):
        form = self.submit_data(form_data(1, 1, 1, 0, num_project_approval_form=0, stages=1))
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_doesnt_validates_with_multiple_project_approval_form(self):
        form = self.submit_data(form_data(1, 1, 1, 0, num_project_approval_form=2, stages=1))
        self.assertFalse(form.is_valid(), form.errors.as_text())
        form = self.submit_data(form_data(1, 1, 1, 0, num_project_approval_form=2, stages=2))
        self.assertFalse(form.is_valid(), form.errors.as_text())
