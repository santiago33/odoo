import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vehicle_ids = fields.One2many(
        comodel_name='as.vehicle',
        inverse_name='partner_id',
        string="Vehicles"
    )




