import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHDiseases(models.Model):
    _name = 'hr.hospital.diseases'
    _description = 'Diseases'

    name = fields.Char()
    description = fields.Text()


