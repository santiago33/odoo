import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHDiagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'
    _rec_name = 'description'

    description = fields.Text()
    is_confirmed = fields.Boolean()

    visit_id = fields.Many2many(
        comodel_name="hr.hospital.visit",
    )
    diseases_id = fields.Many2one(
        comodel_name="hr.hospital.visit",
    )
