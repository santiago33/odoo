import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ASCarBrand(models.Model):
    _name = 'as.car.brand'
    _description = 'Car Manufacture'

    name = fields.Char(
        required=True,
        translate=True,)

    model_ids = fields.One2many(
        comodel_name='as.car.model',
        inverse_name='brand_id',
        string='Car Model'



    )