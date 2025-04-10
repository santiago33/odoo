import logging

from datetime import datetime, time
from odoo.exceptions import ValidationError, UserError
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class HHVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit patient'

    scheduled_date = fields.Datetime(
        required=True,
    )
    completed_date = fields.Datetime()

    status = fields.Selection(
        default="scheduled",
        selection=[
            ('scheduled', _('Scheduled')),
            ('completed', _('Completed')),
            ('cancelled', _('Canceled')),
        ],
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        required=True,
    )
    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        required=True,
    )
    diagnosis_id = fields.Many2one(
        comodel_name='hr.hospital.diagnosis',
        string='Diagnosis',
    )

    @api.constrains('scheduled_date')
    def _check_scheduled_date(self):
        for record in self:
            if record.scheduled_date < datetime.now():
                raise ValidationError(_("Visit is begun"))

    @api.constrains('completed_date', 'status')
    def _check_status(self):
        for record in self:
            if record.status == 'completed' and not record.completed_date:
                raise ValidationError(
                    _('Set completed date for status "completed"'))

    @api.constrains('scheduled_date', 'doctor_id', 'patient_id')
    def _check_visit_uniq_for_day(self):
        for record in self:
            start_d = datetime.combine(record.scheduled_date.date(), time.min)
            end_d = datetime.combine(record.scheduled_date.date(), time.max)
            rec = self.search([
                ('id', '!=', self.id),
                ('scheduled_date', '>=', start_d),
                ('scheduled_date', '<=', end_d),
                ('doctor_id', '=', record.doctor_id.id),
                ('patient_id', '=', record.patient_id.id),
            ])
            if rec:
                raise ValidationError(
                    _('Only one visit to the doctor per day'))

    @api.ondelete(at_uninstall=False)
    def _unlink_visit(self):
        for record in self:
            if record.diagnosis_id:
                raise UserError(_('already have a diagnosis'))

    @api.model
    def get_color_status(self, status):
        classTxt = ''
        if status == 'scheduled':
            classTxt = 'text-warning'
        if status == 'completed':
            classTxt = 'text-success'
        if status == 'cancelled':
            classTxt = 'text-danger'
        return classTxt
