# Generated by Django 2.2.24 on 2021-07-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0055_add_batch_delete_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('UPDATE_LEAD', 'Update Lead'), ('BATCH_UPDATE_LEAD', 'Batch Update Lead'), ('EDIT', 'Edit'), ('APPLICANT_EDIT', 'Applicant Edit'), ('NEW_SUBMISSION', 'New Submission'), ('SCREENING', 'Screening'), ('TRANSITION', 'Transition'), ('BATCH_TRANSITION', 'Batch Transition'), ('DETERMINATION_OUTCOME', 'Determination Outcome'), ('BATCH_DETERMINATION_OUTCOME', 'Batch Determination Outcome'), ('INVITED_TO_PROPOSAL', 'Invited To Proposal'), ('REVIEWERS_UPDATED', 'Reviewers Updated'), ('BATCH_REVIEWERS_UPDATED', 'Batch Reviewers Updated'), ('PARTNERS_UPDATED', 'Partners Updated'), ('PARTNERS_UPDATED_PARTNER', 'Partners Updated Partner'), ('READY_FOR_REVIEW', 'Ready For Review'), ('BATCH_READY_FOR_REVIEW', 'Batch Ready For Review'), ('NEW_REVIEW', 'New Review'), ('COMMENT', 'Comment'), ('PROPOSAL_SUBMITTED', 'Proposal Submitted'), ('OPENED_SEALED', 'Opened Sealed Submission'), ('REVIEW_OPINION', 'Review Opinion'), ('DELETE_SUBMISSION', 'Delete Submission'), ('DELETE_REVIEW', 'Delete Review'), ('CREATED_PROJECT', 'Created Project'), ('UPDATED_VENDOR', 'Updated Vendor'), ('UPDATE_PROJECT_LEAD', 'Update Project Lead'), ('EDIT_REVIEW', 'Edit Review'), ('SEND_FOR_APPROVAL', 'Send for Approval'), ('APPROVE_PROJECT', 'Project was Approved'), ('PROJECT_TRANSITION', 'Project was Transitioned'), ('REQUEST_PROJECT_CHANGE', 'Project change requested'), ('UPLOAD_DOCUMENT', 'Document was Uploaded to Project'), ('REMOVE_DOCUMENT', 'Document was Removed from Project'), ('UPLOAD_CONTRACT', 'Contract was Uploaded to Project'), ('APPROVE_CONTRACT', 'Contract was Approved'), ('REQUEST_PAYMENT', 'Payment was requested for Project'), ('UPDATE_PAYMENT_REQUEST_STATUS', 'Updated Payment Request Status'), ('DELETE_PAYMENT_REQUEST', 'Delete Payment Request'), ('SENT_TO_COMPLIANCE', 'Project was sent to Compliance'), ('UPDATE_PAYMENT_REQUEST', 'Updated Payment Request'), ('SUBMIT_REPORT', 'Submit Report'), ('SKIPPED_REPORT', 'Skipped Report'), ('REPORT_FREQUENCY_CHANGED', 'Report Frequency Changed'), ('REPORT_NOTIFY', 'Report Notify'), ('CREATE_REMINDER', 'Reminder Created'), ('DELETE_REMINDER', 'Reminder Deleted'), ('REVIEW_REMINDER', 'Reminde to Review'), ('BATCH_DELETE_SUBMISSION', 'Delete Batch Submissions')], max_length=50),
        ),
    ]
