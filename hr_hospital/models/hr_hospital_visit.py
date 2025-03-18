import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit patient'

    visit_date = fields.Date()
    is_active = fields.Boolean(default=True, )
    res_doctor_id = fields.Many2one(
        cmodel_name='hr.hospital.doctor',
        string="Doctor",
    )
    res_patient_id = fields.Many2one(
        cmodel_name='hr.hospital.patient',
        string="Patient",
    )
    res_diseases_id = fields.Many2one(
        cmodel_name='hr.hospital.diseases',
        string="Diseases",
    )
