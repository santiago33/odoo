import logging
from dataclasses import fields

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char()
    birthday = fields.Date()
    gender = fields.Char()


