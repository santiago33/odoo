import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_auto_part = fields.Boolean(
        default=False,
        string='Part for car'
    )
