import logging
from re import search

from odoo import models, fields, api
from datetime import datetime, date, time

from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)


class HHVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit patient'

    scheduled_date = fields.Datetime(
        required=True,
    )
    completed_date = fields.Datetime()

    status_id = fields.Selection(
        default="scheduled",
        selection=[('scheduled', 'Scheduled'),
                   ('completed', 'Completed'),
                   ('cancelled', 'Canceled'),
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
                raise ValidationError("Visit is begun")

    @api.constrains('scheduled_date', 'doctor_id', 'patient_id')
    def _check_visit_uniq_for_day(self):
        for record in self:
            rec = self.search([
                ('scheduled_date', '>=',
                 datetime.combine(record.scheduled_date.date(), time.min)),
                ('scheduled_date', '<=',
                 datetime.combine(record.scheduled_date.date(), time.max)),
                ('doctor_id', '=', record.doctor_id.id),
                ('patient_id', '=', record.patient_id.id),
            ])
            if rec:
                raise ValidationError('Only one visit to the doctor per day')

    @api.ondelete(at_uninstall=False)
    def _unlink_visit(self):
        for record in self:
            if record.diagnosis_id:
                raise UserError('already have a diagnosis')
