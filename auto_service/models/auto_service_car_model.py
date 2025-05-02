import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ASCarModel(models.Model):
    _name = 'as.car.model'
    _description = 'Car model'

    name = fields.Char(
        required=True,
        translate=True,
    )
    start_date = fields.Date()
    end_date = fields.Date()
    brand_id = fields.Many2one(
        comodel_name='as.car.brand',
        string='Car manufacture',
        required=True,
    )
