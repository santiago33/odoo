import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char()
    profession = fields.Char()
    work_experience = fields.Integer()


