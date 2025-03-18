import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit patient'

    visit_date = fields.Date()
    is_active = fields.Boolean(default=True, )
    doctor_id = fields.Many2one(
        cmodel_name='hr.hospital.doctor',
    )
    patient_id = fields.Many2one(
        cmodel_name='hr.hospital.patient',
    )
    diseases_id = fields.Many2one(
        cmodel_name='hr.hospital.diseases',
    )
